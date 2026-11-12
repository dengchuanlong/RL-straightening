# RL straightening: manuscript data and code

This public repository contains the supporting data, analysis code and finite-element reference materials for the PLOS ONE manuscript **Reinforcement learning for straightening stroke prediction under unloaded geometry constraints**. The source manuscript is identified by SHA-256 `8531d24f18558dff9885d43321e797888bcd1ff111f3bf129d908063536a9ae6`; the DOCX itself is not duplicated here.

## Contents

| Path | Contents | Manuscript link |
|---|---|---|
| `supporting_information/S1_File.zip` | Experiment 1 reduced-order simulation, five-seed policies, results, figure data, code and reproduction instructions. | S1 File; Experiment 1, Figs 1–3 and Tables 1–3. |
| `supporting_information/S2_File.zip.parts/` | Numbered raw-byte parts of S2. | S2 File; Experiment 2 surrogate/policy data, code and analysis. |
| `supporting_information/S3_File.zip.parts/` | Numbered raw-byte parts of S3. | S3 File; three new RL-action finite-element records. |
| `supporting_information/S4_File.zip.parts/` | Numbered raw-byte parts of S4. | S4 File; paired direct-optimization finite-element records. |
| `engineering/` | The manuscript reference-32 engineering release at commit `0960d0fcbf32a5824725853d7d381f7feeeeb22d`; the software ZIP is stored as numbered raw-byte parts. | Reference 32. |
| `assemble_archives.py` | Rebuilds the original S2–S4 and reference-32 ZIPs and verifies their original SHA-256 values. | Reproducibility. |
| `repo_manifest.json`, `DATA_PROVENANCE.md`, `SHA256SUMS` | Provenance, path map and integrity records. | Data availability. |

Run `python assemble_archives.py` from the repository root to reconstruct the split ZIP files at their original paths. The reconstructed archives are byte-identical to the author-provided files and are checked against their original sizes and SHA-256 hashes. S1 is already present as a single ZIP.

## Reference 32 data and code

Reference 32 cites `dengchuanlong/straightening` at commit `0960d0fcbf32a5824725853d7d381f7feeeeb22d`, path `engineering/FE_REFERENCE_METHODS.md`. The complete `engineering/` release is included: its text, tabular data, metadata, notices, checksum and verification records are byte-for-byte mirrors; `Supplementary_Software_1.zip` is represented by numbered raw-byte parts and reassembles to the original file with the source SHA-256 in `engineering/Supplementary_Software_1.zip.sha256`.

The included OPARA-288 material remains subject to its original **CC BY-NC 4.0** terms. Preserve the attribution and conditions in `engineering/THIRD_PARTY_DATA_NOTICE.txt` and `engineering/third_party/OPARA_288_original_dataset_metadata.txt`. This repository does not relicense that material or assert a blanket licence for the software, data or ANSYS.

## Reproduction scope

Follow the README files inside each reconstructed supporting archive. S1 contains code and data for the reported reduced-order results. S2–S4 contain data and analysis code for the reported profile and native finite-element actions. The paper records that large native result/restart binaries and full integration-point fields are excluded; the compact files support the reported geometric analyses without ANSYS. Historical warm restarts require compatible licensed ANSYS and the separately retained checkpoints.

The manuscript's inherited 9,000-row analytical dataset and the archived FE-profile records are separate sources; the manuscript states that the 9,000-row table was not used to construct the profile surrogate. No DOI or project-wide licence is asserted here.
