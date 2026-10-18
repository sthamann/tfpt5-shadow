"""Kernel freeze guard: every kernel number must be the exact axiom consequence
and byte-match the sibling searches (repeater-cascade / comb-meta-limit /
pulsar-glitch-recovery). Editing these values invalidates the prereg."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from p9_forecast import constants as c  # noqa: E402


def test_axioms():
    assert c.C3 == 1.0 / (8.0 * math.pi)
    assert c.G_CAR == 5


def test_cascade_kernel_exact():
    assert c.LAMBDA_CASCADE == 11.390625                       # (3/2)^6 exact binary
    assert abs(c.OMEGA - 2.5827069463082895) < 1e-15
    assert abs(c.EPS_PREDICTED - 0.01730246011431484) < 1e-17
    assert abs(c.GW_ECHO_CEILING - (2.0 / 3.0) ** 6) < 1e-18
    assert abs(c.GW_ECHO_CEILING - 0.08779149519890261) < 1e-15


def test_gates_frozen():
    assert c.REACH_GATE_PERIODS == 2.8
    assert c.EPS_REFERENCE == 0.30
    assert c.DETECTION_ALPHA == 0.05
    assert c.POWER_GATE == 0.80


def test_matches_sibling_constants():
    """Byte-match against the repeater-cascade frozen layer if importable."""
    sib = Path(__file__).resolve().parents[2] / "repeater-cascade" / "src"
    if not sib.exists():
        return
    sys.path.insert(0, str(sib))
    try:
        from repeater_cascade import constants as rc
    except ImportError:
        return
    assert rc.OMEGA == c.OMEGA
    assert rc.EPS_PREDICTED == c.EPS_PREDICTED
    assert rc.LAMBDA_CASCADE == c.LAMBDA_CASCADE
    assert rc.REACH_GATE_PERIODS == c.REACH_GATE_PERIODS


if __name__ == "__main__":
    for fn in (test_axioms, test_cascade_kernel_exact, test_gates_frozen,
               test_matches_sibling_constants):
        fn()
        print(f"{fn.__name__}: PASS")
