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
passes literally on the export) but **not** `website/`. The single-source generator
`verification/make_script_index.py` detects the missing `website/` and skips its `ScriptIndex.tsx`
mirror, so `bash build.sh notes` runs on the subset without it.

**Do not edit here.** Changes flow: main repo → this mirror (GitHub Action) → Overleaf pull.

Source: `sthamann/tfpt-theoryv4` @ `55cd5be9d13b6faba812db9383cb3a526b5a83c7`
Last export: 2026-06-25 11:28:30Z
Files exported: 981
