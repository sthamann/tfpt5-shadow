#!/usr/bin/env python3
"""Fetch script for the FUTURE data pass (documented, not executed at
the preregistered stage -- running it is the moment 'data contact'
begins and must be logged in the project README).

Planned public sources (Planck Legacy Archive / IRSA):
  SMICA     https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica_2048_R3.00_full.fits
  Commander https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-commander_2048_R3.00_full.fits
  NILC      https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-nilc_2048_R3.00_full.fits
  Mask      common temperature confidence mask from the same release
"""

if __name__ == "__main__":
    print(__doc__)
    print("NOT downloading: preregistered stage (see README firewall).")
    raise SystemExit(3)
