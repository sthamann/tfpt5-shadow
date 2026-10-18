#!/usr/bin/env python3
"""Audit the proposed charged-lepton theta13 identification.

EXPLORATION ONLY.  This is one pre-declared, deterministic identification
test, not a value census:

    required |Y_3e|/y_3 = 0.1520145886
    proposed identity   = sqrt(phi0 * exp(-5/6)).

The numerical comparison is admissible only if the requirement was derived
without inserting the proposed TFPT reactor angle.  Provenance is therefore
part of the test.  If provenance is circular, the complete-texture, v3-freeze,
and leptogenesis branches are not evaluated.  The fixed companion value
2*phi0**2 is still printed for honest accounting, but it is not promoted to a
second identification after a circularity kill.
"""

from __future__ import annotations

import ast
import os
import sys
from dataclasses import dataclass

import mpmath as mp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
RATIO_PROBE = os.path.join(HERE, "nu_ratio_grammar_probe.py")
V3_HYPOTHESIS = os.path.join(
    REPO,
    "experiments",
    "nu-scalaron-falsification",
    "hypotheses",
    "nu_scalaron_v3.yaml",
)
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import phi0  # noqa: E402


mp.mp.dps = 60

PHI0 = mp.mpf(phi0)
REQUIRED_Y3E_OVER_Y3 = mp.mpf("0.1520145886")
REQUIRED_Y3E_BAND = (mp.mpf("0.15009"), mp.mpf("0.15391"))
IDENTIFICATION_MAX_RELATIVE_DEVIATION = mp.mpf("0.001")

# Independent NuFIT central value named in the task.  The audited ratio probe
# does not use this central value in T3; it uses only a sigma around TFPT T3.
NUFIT_SIN2_THETA13 = mp.mpf("0.02195")

# T1 is independently data-inverted in nu_ratio_grammar_probe.py.
REQUIRED_Y2_OVER_Y3 = mp.mpf("0.005572598413861311")
REQUIRED_Y2_OVER_Y3_BAND = (
    mp.mpf("0.0054556776"),
    mp.mpf("0.0056895192"),
)


@dataclass(frozen=True)
class ProvenanceAudit:
    sin2_expression: str
    s13_expression: str
    target_expression: str
    lower_expression: str
    upper_expression: str
    tfpt_central_inserted: bool
    nufit_central_inserted: bool
    nufit_sigma_only: bool

    @property
    def verdict(self) -> str:
        if self.tfpt_central_inserted:
            return "CIRCULAR"
        return "NON_CIRCULAR"


def named_assignments(tree: ast.AST) -> dict[str, ast.AST]:
    """Return simple named assignments from the audited source."""
    assignments: dict[str, ast.AST] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
    return assignments


def keyword_expression(call: ast.AST, name: str) -> ast.AST:
    if not isinstance(call, ast.Call):
        raise AssertionError(f"expected call while resolving keyword {name}")
    for keyword in call.keywords:
        if keyword.arg == name:
            return keyword.value
    raise AssertionError(f"missing keyword {name}")


def compact(expression: ast.AST) -> str:
    return ast.unparse(expression).replace(" ", "")


def audit_t3_provenance() -> ProvenanceAudit:
    """Trace T3's central value and band directly through the source AST."""
    with open(RATIO_PROBE, encoding="utf-8") as source_file:
        source = source_file.read()
    assignments = named_assignments(ast.parse(source, filename=RATIO_PROBE))

    sin2_node = assignments["sin2_theta13"]
    s13_node = assignments["s13"]
    t3_node = assignments["t3"]
    target_node = keyword_expression(t3_node, "target")
    lower_node = assignments["t3_lower"]
    upper_node = assignments["t3_upper"]

    sin2_compact = compact(sin2_node)
    s13_compact = compact(s13_node)
    target_compact = compact(target_node)
    lower_compact = compact(lower_node)
    upper_compact = compact(upper_node)

    tfpt_central_inserted = (
        "PHI0" in sin2_compact
        and "mp.exp" in sin2_compact
        and "sin2_theta13" in s13_compact
        and target_compact == "s13"
    )
    nufit_central_inserted = "0.02195" in source
    nufit_sigma_only = (
        "SIN2_THETA13_SIGMA" in lower_compact
        and "SIN2_THETA13_SIGMA" in upper_compact
        and not nufit_central_inserted
    )
    return ProvenanceAudit(
        sin2_expression=ast.unparse(sin2_node),
        s13_expression=ast.unparse(s13_node),
        target_expression=ast.unparse(target_node),
        lower_expression=ast.unparse(lower_node),
        upper_expression=ast.unparse(upper_node),
        tfpt_central_inserted=tfpt_central_inserted,
        nufit_central_inserted=nufit_central_inserted,
        nufit_sigma_only=nufit_sigma_only,
    )


def relative_deviation(value: mp.mpf, reference: mp.mpf) -> mp.mpf:
    return value / reference - 1


def fmt(value: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(value, digits)


def percent(value: mp.mpf) -> str:
    return f"{float(100 * value):+.9f}%"


def main() -> int:
    print("PRE-DECLARED SINGLE IDENTIFICATION TEST (NOT A CENSUS)")
    print("  H0: 0.1520145886 = sqrt(phi0 * exp(-5/6))")
    print("  admissibility: provenance must be NON_CIRCULAR")
    print("  numerical threshold: |relative deviation| < 0.1%")
    print("  kill rule: circular provenance stops texture/freeze/leptogenesis")
    print()

    provenance = audit_t3_provenance()
    tfpt_sin2_theta13 = PHI0 * mp.exp(-mp.mpf(5) / 6)
    tfpt_sin_theta13 = mp.sqrt(tfpt_sin2_theta13)
    nufit_sin_theta13 = mp.sqrt(NUFIT_SIN2_THETA13)
    companion_ratio = 2 * PHI0**2

    tfpt_deviation = relative_deviation(
        tfpt_sin_theta13, REQUIRED_Y3E_OVER_Y3
    )
    nufit_deviation = relative_deviation(
        nufit_sin_theta13, REQUIRED_Y3E_OVER_Y3
    )
    companion_deviation = relative_deviation(
        companion_ratio, REQUIRED_Y2_OVER_Y3
    )

    print("NUMERICAL COMPARISONS")
    print(
        "  TFPT sqrt(phi0*exp(-5/6))={} vs required={} rel={}".format(
            fmt(tfpt_sin_theta13),
            fmt(REQUIRED_Y3E_OVER_Y3),
            percent(tfpt_deviation),
        )
    )
    print(
        "  NuFIT sqrt(0.02195)={} vs required={} rel={}".format(
            fmt(nufit_sin_theta13),
            fmt(REQUIRED_Y3E_OVER_Y3),
            percent(nufit_deviation),
        )
    )
    print(
        "  companion 2*phi0^2={} vs required y2/y3={} rel={}".format(
            fmt(companion_ratio),
            fmt(REQUIRED_Y2_OVER_Y3),
            percent(companion_deviation),
        )
    )
    print(
        "  bands: theta13={} y2/y3={}".format(
            tuple(fmt(value, 12) for value in REQUIRED_Y3E_BAND),
            tuple(fmt(value, 12) for value in REQUIRED_Y2_OVER_Y3_BAND),
        )
    )
    print()

    print("T3 PROVENANCE TRACE")
    print(f"  sin2_theta13 <- {provenance.sin2_expression}")
    print(f"  s13           <- {provenance.s13_expression}")
    print(f"  T3.target      <- {provenance.target_expression}")
    print(f"  T3.lower       <- {provenance.lower_expression}")
    print(f"  T3.upper       <- {provenance.upper_expression}")
    print(
        "  NuFIT central inserted={} ; NuFIT sigma-only band={}".format(
            provenance.nufit_central_inserted, provenance.nufit_sigma_only
        )
    )
    print("CIRCULARITY_VERDICT", provenance.verdict)
    print(
        "  The T3 central requirement is the TFPT formula itself; the source "
        "did not derive 0.1520145886 from NuFIT central data. NuFIT supplies "
        "only the uncertainty used to draw a band around that inserted center."
    )
    print()

    numeric_match = (
        abs(tfpt_deviation) < IDENTIFICATION_MAX_RELATIVE_DEVIATION
        and REQUIRED_Y3E_BAND[0]
        <= tfpt_sin_theta13
        <= REQUIRED_Y3E_BAND[1]
    )
    identification_admissible = provenance.verdict == "NON_CIRCULAR"
    zero_dial_chain_identified = numeric_match and identification_admissible

    print("DECISION")
    print("  numeric_match_below_0.1pct", numeric_match)
    print("  identification_admissible", identification_admissible)
    print("  zero_dial_chain_identified", zero_dial_chain_identified)
    print(
        "  companion_status CONDITIONAL_NOT_ACTIVATED "
        "(deviation reported; no second identification claim)"
    )
    print("  complete_texture SKIPPED_CIRCULARITY_KILL")
    print("  v3_freeze NOT_CREATED")
    print("  eta_B_update NOT_RUN_NO_ADMISSIBLE_V3_TEXTURE")
    print(
        "  boundary tree-level seesaw; charged-lepton/Q+ basis map remains "
        "unfrozen; FLAV.NUSCALE.05 remains [O]"
    )
    print("VERDICT NU_THETA13_CHARGED_LEPTON_CIRCULAR_KILL")
    print()

    checks = [
        (
            "TFPT value is inside declared magnitude band",
            REQUIRED_Y3E_BAND[0]
            <= tfpt_sin_theta13
            <= REQUIRED_Y3E_BAND[1],
        ),
        (
            "numeric equality is below 0.1% threshold",
            abs(tfpt_deviation) < IDENTIFICATION_MAX_RELATIVE_DEVIATION,
        ),
        ("AST trace finds TFPT central inserted", provenance.tfpt_central_inserted),
        ("NuFIT central is absent from T3 derivation", not provenance.nufit_central_inserted),
        ("NuFIT contribution is sigma-only", provenance.nufit_sigma_only),
        ("circular match is not promoted", not zero_dial_chain_identified),
        ("companion value is inside the pre-existing T1 band", REQUIRED_Y2_OVER_Y3_BAND[0] <= companion_ratio <= REQUIRED_Y2_OVER_Y3_BAND[1]),
        ("no v3 hypothesis was created", not os.path.exists(V3_HYPOTHESIS)),
    ]
    for label, passed in checks:
        print(("PASS " if passed else "FAIL ") + label)
    all_pass = all(passed for _label, passed in checks)
    print("PROTOCOL-ALL-PASS" if all_pass else "PROTOCOL-FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
