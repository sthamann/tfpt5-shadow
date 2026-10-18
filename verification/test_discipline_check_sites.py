"""Regression tests for v649's static check-site counter."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


VERIFICATION_DIR = Path(__file__).resolve().parent
if str(VERIFICATION_DIR) not in sys.path:
    sys.path.insert(0, str(VERIFICATION_DIR))

import v649_discipline_audit as audit


class CheckSiteCountTests(unittest.TestCase):
    def test_real_tfpt_check_alias_counts_once(self) -> None:
        source = (
            "from tfpt_constants import check as suite_check\n"
            "suite_check('real', True)\n"
        )
        self.assertEqual(audit.check_site_count(source), 1)

    def test_aliased_call_in_comment_does_not_count(self) -> None:
        source = (
            "from tfpt_constants import check as suite_check\n"
            "# suite_check('comment only', True)\n"
        )
        self.assertEqual(audit.check_site_count(source), 0)

    def test_aliased_call_in_string_does_not_count(self) -> None:
        source = (
            "from tfpt_constants import check as suite_check\n"
            "text = \"suite_check('string only', True)\"\n"
        )
        self.assertEqual(audit.check_site_count(source), 0)

    def test_empty_source_does_not_count(self) -> None:
        self.assertEqual(audit.check_site_count(""), 0)

    def test_assert_only_source_does_not_count(self) -> None:
        self.assertEqual(audit.check_site_count("assert True\n"), 0)

    def test_unrelated_import_using_same_alias_does_not_count(self) -> None:
        source = (
            "from unrelated_harness import check as suite_check\n"
            "suite_check('not tfpt_constants', True)\n"
        )
        self.assertEqual(audit.check_site_count(source), 0)

    def test_legacy_local_check_counts_once(self) -> None:
        source = "def check(value):\n    return value\n\ncheck(True)\n"
        self.assertEqual(audit.check_site_count(source), 1)


if __name__ == "__main__":
    unittest.main()
