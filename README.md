# RL straightening: manuscript data and code

This public repository contains the supporting data, analysis code and finite-element reference materials for the manuscript **Reinforcement learning for straightening stroke prediction under unloaded geometry constraints**. 

## Contents

| Path | Contents | Manuscript link |
|---|---|---|
| `supporting_information/S1_File.zip` | Experiment 1 reduced-order simulation, five-seed policies, results, figure data, code and reproduction instructions. | S1 File; Experiment 1, Figs 1–3 and Tables 1–3. |
| `supporting_information/S2_File.zip.parts/` | Numbered raw-byte parts of S2. | S2 File; Experiment 2 surrogate/policy data, code and analysis. |
| `supporting_information/S3_File.zip.parts/` | Numbered raw-byte parts of S3. | S3 File; three new RL-action finite-element records. |
| `supporting_information/S4_File.zip.parts/` | Numbered raw-byte parts of S4. | S4 File; paired direct-optimization finite-element records. |
| `assemble_archives.py` | Rebuilds the original S2–S4 and reference-32 ZIPs and verifies their original SHA-256 values. | Reproducibility. |
| `repo_manifest.json`, `DATA_PROVENANCE.md`, `SHA256SUMS` | Provenance, path map and integrity records. | Data availability. |

Run `python assemble_archives.py` from the repository root to reconstruct the split ZIP files at their original paths. The reconstructed archives are byte-identical to the author-provided files and are checked against their original sizes and SHA-256 hashes. S1 is already present as a single ZIP.


## Reproduction scope

Follow the README files inside each reconstructed supporting archive. S1 contains code and data for the reported reduced-order results. S2–S4 contain data and analysis code for the reported profile and native finite-element actions. The paper records that large native result/restart binaries and full integration-point fields are excluded; the compact files support the reported geometric analyses without ANSYS. Historical warm restarts require compatible licensed ANSYS and the separately retained checkpoints.
