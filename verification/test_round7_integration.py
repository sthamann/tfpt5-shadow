"""Integration regressions for the native Round-7 verifier ports.

These tests protect import, entrypoint, source-root, and check-harness wiring.
The expected counts are integration invariants; they are not substitutes for
the exact identities and explicit claim boundaries inside the verifiers.
"""

from __future__ import annotations

import ast
import contextlib
import importlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


VERIFICATION_DIR = Path(__file__).resolve().parent
if str(VERIFICATION_DIR) not in sys.path:
    sys.path.insert(0, str(VERIFICATION_DIR))

EXPECTED = {
    "v1031_quantum_tensor_curvature": ("v1031 quantum tensor curvature", 69),
    "v1032_covariant_curvature": ("v1032 covariant curvature", 34),
    "v1033_charged_disorder": ("v1033 charged disorder", 35),
    "v1034_parent_mirror": ("v1034 parent mirror", 36),
    "v1035_matter_coupling": ("v1035 matter coupling", 59),
}
SOURCE_READERS = {
    "v1033_charged_disorder": (
        "verification/v983_simple_current_generator.py",
        "verification/v988_psi_lambda_reduction.py",
        "articles/2026-08-30/mmst_charged_scaling_limit_en.tex",
    ),
    "v1034_parent_mirror": (
        "verification/v1002_spin10_mirror_projector.py",
        "verification/v1008_master_assembly_scaffold.py",
        "verification/v1024_parent_internal_boundaries.py",
        "verification/v1027_signed_det_car_wall.py",
    ),
}


def module_path(name: str) -> Path:
    return VERIFICATION_DIR / f"{name}.py"


def module_source(name: str) -> str:
    return module_path(name).read_text(encoding="utf-8")


def subprocess_environment(**updates: str) -> dict[str, str]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment.update(updates)
    return environment


class Round7NativeIntegrationTests(unittest.TestCase):
    def test_imports_are_silent_and_do_not_execute_verifiers(self) -> None:
        imports = "; ".join(f"import {name}" for name in EXPECTED)
        code = (
            "import sys; "
            f"sys.path.insert(0, {str(VERIFICATION_DIR)!r}); "
            f"{imports}"
        )
        with tempfile.TemporaryDirectory() as working_directory:
            completed = subprocess.run(
                [sys.executable, "-c", code],
                cwd=working_directory,
                env=subprocess_environment(),
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout, "")
        self.assertEqual(completed.stderr, "")

    def test_native_entrypoint_contract_and_provenance(self) -> None:
        for name in EXPECTED:
            with self.subTest(module=name):
                source = module_source(name)
                tree = ast.parse(source)
                imports = [
                    node
                    for node in tree.body
                    if isinstance(node, ast.ImportFrom)
                    and node.module == "tfpt_constants"
                ]
                self.assertEqual(len(imports), 1)
                aliases = {
                    alias.name: alias.asname
                    for alias in imports[0].names
                }
                self.assertEqual(
                    aliases,
                    {"check": "suite_check", "reset": None, "summary": None},
                )

                functions = {
                    node.name: node
                    for node in tree.body
                    if isinstance(node, ast.FunctionDef)
                }
                self.assertIn("run", functions)
                self.assertNotIn("main", functions)
                run_calls = {
                    node.func.id
                    for node in ast.walk(functions["run"])
                    if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                }
                self.assertIn("reset", run_calls)
                self.assertIn("summary", run_calls)

                guards = [
                    node
                    for node in tree.body
                    if isinstance(node, ast.If)
                    and isinstance(node.test, ast.Compare)
                    and ast.unparse(node.test) == "__name__ == '__main__'"
                ]
                self.assertEqual(len(guards), 1)
                self.assertEqual(
                    ast.unparse(guards[0].body[0]),
                    "raise SystemExit(run())",
                )

                docstring = ast.get_docstring(tree) or ""
                self.assertIn("Port provenance:", docstring)
                self.assertRegex(docstring, r"source SHA-256 [0-9a-f]{64}")

    def test_no_personal_paths_and_native_source_frontends_are_declared(self) -> None:
        personal_path_markers = (
            "".join(("/", "Users", "/")),
            "".join(("/", "home", "/")),
            "".join(("\\", "Users", "\\")),
        )
        for name in EXPECTED:
            with self.subTest(module=name):
                source = module_source(name)
                for marker in personal_path_markers:
                    self.assertNotIn(marker, source)

        dynamic_root = "DEFAULT_REPO = Path(__file__).resolve().parents[1]"
        dynamic_override = (
            'REPO = Path(os.environ.get("TFPT_REPO", str(DEFAULT_REPO))).resolve()'
        )
        for name, required_frontends in SOURCE_READERS.items():
            with self.subTest(source_reader=name):
                source = module_source(name)
                self.assertIn(dynamic_root, source)
                self.assertIn(dynamic_override, source)
                for relative_path in required_frontends:
                    self.assertIn(relative_path, source)

        for name in set(EXPECTED) - set(SOURCE_READERS):
            with self.subTest(native_only=name):
                self.assertNotIn("TFPT_REPO", module_source(name))

        website = VERIFICATION_DIR.parent / "website"
        runtime_source = (website / "lib/pyodide.ts").read_text(encoding="utf-8")
        for name in SOURCE_READERS:
            self.assertIn(f'"{name}.py":', runtime_source)
        dialog_source = (website / "components/Reproducer.tsx").read_text(encoding="utf-8")
        self.assertNotIn("Native Arb/Acb certificate", dialog_source)
        self.assertIn("full local repository environment", dialog_source)

    def test_native_execution_wiring_preserves_declared_counts(self) -> None:
        # One bounded subprocess avoids multiplying interpreter/import overhead.
        code = f"""
import importlib
import json
import sys
sys.path.insert(0, {str(VERIFICATION_DIR)!r})
names = {list(EXPECTED)!r}
returns = {{}}
for name in names:
    returns[name] = importlib.import_module(name).run()
print("ROUND7_RETURN_CODES=" + json.dumps(returns, sort_keys=True))
raise SystemExit(1 if any(returns.values()) else 0)
"""
        with tempfile.TemporaryDirectory() as working_directory:
            completed = subprocess.run(
                [sys.executable, "-c", code],
                cwd=working_directory,
                env=subprocess_environment(),
                capture_output=True,
                text=True,
                timeout=180,
                check=False,
            )
        self.assertEqual(
            completed.returncode, 0,
            completed.stdout + "\nSTDERR:\n" + completed.stderr,
        )
        self.assertEqual(sum(count for _, count in EXPECTED.values()), 233)
        for title, count in EXPECTED.values():
            self.assertIn(
                f"--- {title}: {count} passed, 0 failed ---",
                completed.stdout,
            )
        marker = "ROUND7_RETURN_CODES="
        line = next(
            (row for row in completed.stdout.splitlines() if row.startswith(marker)),
            None,
        )
        self.assertIsNotNone(line)
        self.assertEqual(
            json.loads(line[len(marker):]),
            {name: 0 for name in EXPECTED},
        )

    def test_quick_verifiers_reset_on_repeated_run(self) -> None:
        for name in ("v1034_parent_mirror", "v1035_matter_coupling"):
            title, count = EXPECTED[name]
            module = importlib.import_module(name)
            outputs = []
            returns = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    returns.append(module.run())
                outputs.append(stream.getvalue())
            with self.subTest(module=name):
                expected_summary = (
                    f"--- {title}: {count} passed, 0 failed ---"
                )
                self.assertEqual(returns, [0, 0])
                self.assertEqual(
                    [output.strip().splitlines()[-1] for output in outputs],
                    [expected_summary, expected_summary],
                )

    def test_degenerate_half_filling_is_basis_independent(self) -> None:
        module = importlib.import_module("v1033_charged_disorder")
        np = module.np
        h = np.diag([-2.0, 0.0, 0.0, 2.0])
        values, vectors = np.linalg.eigh(h)
        expected = np.diag([1.0, 0.5, 0.5, 0.0])
        for angle in (0.0, 0.37, 1.2):
            rotated = vectors.copy()
            c, s = np.cos(angle), np.sin(angle)
            rotated[:, 1:3] = vectors[:, 1:3] @ np.array([[c, -s], [s, c]])
            with patch.object(module.np.linalg, "eigh", return_value=(values, rotated)):
                energy, covariance = module.half_filled_data(h)
                _, _, zero_vectors, remaining = module.half_filled_ground_space(h)
            with self.subTest(angle=angle):
                self.assertAlmostEqual(energy, -2.0)
                np.testing.assert_allclose(covariance, expected, atol=1e-14)
                self.assertAlmostEqual(float(np.trace(covariance)), 2.0)
                bounds = module.ground_space_excess_bounds(
                    covariance, zero_vectors, remaining,
                    np.diag([0.0, -1.0, 3.0, 0.0]), 0.0,
                )
                np.testing.assert_allclose(bounds, (-1.0, 3.0), atol=1e-14)
        for filling, expected_bound in ((0, 0.0), (2, 2.0)):
            zero_vectors = np.eye(2)
            covariance = (filling / 2) * np.eye(2)
            bounds = module.ground_space_excess_bounds(
                covariance, zero_vectors, filling, np.diag([-1.0, 3.0]), 0.0,
            )
            np.testing.assert_allclose(bounds, (expected_bound, expected_bound), atol=1e-14)

    def test_invalid_repo_override_fails_closed(self) -> None:
        green_markers = (
            "VERDICT PASS",
            '"status": "PASS"',
            "SUMMARY: 36 passed, 0 failed",
            "--- v1033 charged disorder: 35 passed, 0 failed ---",
            "--- v1034 parent mirror: 36 passed, 0 failed ---",
        )
        for name in SOURCE_READERS:
            with self.subTest(module=name):
                with tempfile.TemporaryDirectory() as empty_repo:
                    completed = subprocess.run(
                        [sys.executable, str(module_path(name))],
                        cwd=empty_repo,
                        env=subprocess_environment(TFPT_REPO=empty_repo),
                        capture_output=True,
                        text=True,
                        timeout=10,
                        check=False,
                    )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0)
                for marker in green_markers:
                    self.assertNotIn(marker, output)


if __name__ == "__main__":
    unittest.main()
