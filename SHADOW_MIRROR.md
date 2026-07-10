# tfpt5-shadow (auto-generated mirror)

This repository is a **one-way mirror** of the main TFPT repository, maintained for
[Overleaf GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).

| Included | Excluded |
|----------|----------|
| Active `.tex` papers, `tex-artefacts/`, `figures/*.pdf` | `_archive/`, `website/` |
| `verification/` (Python suite, ledger, maps, redteam, wolfram) | `.cursor/`, `.github/` |
| `experiments/` (Lean, discovery) | Compiled paper `*.pdf` (non-figure) |
| `build.sh`, manifests, README | |

**Shadow-mode note.** This subset ships `figures/` (so `python3 verification/make_manifest.py --check`
passes literally on the export) but **not** `website/`. The single-source generators
(`verification/make_script_index.py`, `make_changelog_web.py`, `make_docs_map.py`) detect the
missing `website/` and skip their website mirrors (`ScriptIndex.tsx`, `lib/changelog.ts`,
`website_map.csv`), so `bash build.sh notes` and `bash build.sh gen` run on the subset
non-destructively. `bash build.sh audit` is likewise shadow-aware: it skips the website mirror,
website version and website wolfram-page checks and prints which sections it skipped.

**Export coherence gate.** `scripts/export-shadow.sh` re-runs `make_manifest.py --check` and the
(shadow-aware) `audit_sync.py` on this filtered tree before the mirror is published, so a package
that says \"ALL CHECKS PASSED\" cannot ship unless it actually reproduces as exported.

**Do not edit here.** Changes flow: main repo → this mirror (GitHub Action) → Overleaf pull.

Source: `sthamann/tfpt-theoryv4` @ `5f884c8e2d338ebf6a315c3fa59f8f03736694d4`
Last export: 2026-07-10 11:18:24Z
Files exported: 1359
