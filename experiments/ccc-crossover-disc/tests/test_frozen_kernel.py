"""Guards of the frozen CCC crossover-disc kernel.

These tests fail if anyone silently changes the frozen constants, the
spec strings, or the derived template class."""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ccc_disc import kernel  # noqa: E402


def test_rates_are_exact_rationals():
    assert np.isclose(np.exp(-kernel.DELTA2), 64.0 / 729.0, rtol=1e-14)
    assert np.isclose(np.exp(-kernel.DELTA3), 1.0 / 729.0, rtol=1e-14)
    assert np.isclose(kernel.RATE_RATIO, np.log(3) / np.log(1.5),
                      rtol=1e-14)


def test_overlap_table_frozen():
    assert np.isclose(kernel.C2_PAIR, 1 / np.sqrt(2))
    assert np.isclose(kernel.C3_PAIR, 1 / np.sqrt(6))
    assert kernel.C2_ANCHOR == 0.0
    assert np.isclose(kernel.C3_ANCHOR, -2 / np.sqrt(6))
    assert np.isclose(kernel.C2_PAIR / kernel.C3_PAIR, np.sqrt(3))


def test_theta_max_in_frozen_band():
    assert 1.0 <= kernel.theta_max_deg() <= 1.3


def test_kappa_band_gives_tophat():
    u = kernel.u_rec_band()
    assert max(u.values()) < 1e-4
    assert kernel.contrast_bound() < 5e-4


def test_freeze_hashes_intact():
    for name, (got, exp, ok) in kernel.freeze_status().items():
        assert ok, f"freeze {name} broken: {got} != {exp}"
