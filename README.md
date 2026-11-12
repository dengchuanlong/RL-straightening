# RL straightening: manuscript data and code

This public repository contains the data, analysis code, supporting evidence and finite-element reference package for the PLOS ONE manuscript **Reinforcement learning for straightening stroke prediction under unloaded geometry constraints**. The source manuscript is identified by SHA-256 `8531d24f18558dff9885d43321e797888bcd1ff111f3bf129d908063536a9ae6`; the manuscript itself is not duplicated here.

## Contents

| Path | Contents | Manuscript link |
|---|---|---|
| `supporting_information/S1_File.zip` | Reduced-order simulation, five-seed RL policies, complete condition-level results, figure source data, code and reproduction instructions. | S1 File; Experiment 1, Figs 1–3 and Tables 1–3. |
| `supporting_information/S2_File.zip` | FE-profile surrogate training, frozen policies/actions, profile and native result data, analysis code and methods. | S2 File; Experiment 2, Figs 4–6 and Tables 2–3. |
| `supporting_information/S3_File.zip` | Native finite-element evidence for the three RL-selected actions, including inputs, profiles, solver records and audits. | S3 File. |
| `supporting_information/S4_File.zip` | Paired native finite-element evidence for the three direct-surrogate-optimization actions. | S4 File. |
| `engineering/` | Exact mirror of the complete `engineering/` path cited in manuscript reference 32, from the pinned source commit documented below. | Reference 32; archived FE methods, reference cases and Supplementary Software 1. |
| `repo_manifest.json` | Source-manuscript identity, file hashes, archive sizes and reference-32 provenance. | Provenance. |
| `SHA256SUMS` | SHA-256 checksums of the repository files other than this checksum list. | Integrity. |

The S1–S4 ZIP files are byte-identical to the supporting files prepared with the manuscript. Extract each archive to inspect its CSV data, model inputs, frozen policies, scripts and README files. The supplementary packages are below 20 MB each.

## Reference 32 data and code

Manuscript reference 32 points to `dengchuanlong/straightening` at commit `0960d0fcbf32a5824725853d7d381f7feeeeb22d`, specifically `engineering/FE_REFERENCE_METHODS.md`. This repository mirrors **the full `engineering/` directory at that exact commit, preserving every relative path and file byte-for-byte**. It includes the cited methods, reference cases, verification records, the Supplementary Software 1 archive and its third-party attribution notice. The source commit and per-file hashes are recorded in `repo_manifest.json`.

The included third-party OPARA-288 material remains subject to its original **CC BY-NC 4.0** terms. The notice and source metadata remain in `engineering/`; this repository does not relicense that material or assert a blanket licence for the software, data or ANSYS. Review `engineering/THIRD_PARTY_DATA_NOTICE.txt` before reuse.

## Reproduction scope

Follow the README files inside each supporting archive. S1 contains the numerical simulation, training and verification code plus the data required to reproduce the reported reduced-order results. S2–S4 contain data and analysis code for the reported profile and native finite-element actions. The paper identifies omitted large native result/restart binaries and full integration-point fields; reproducing historical warm restarts also requires compatible licensed ANSYS and the separately retained checkpoint files. The compact files support the reported geometric analyses without ANSYS.

The inherited 9,000-row analytical dataset and the archived FE-profile records are separate data sources. The manuscript states that the 9,000-row table was not used to construct the profile surrogate. Reference 32's `engineering/` archive is included as a separate, byte-preserved source package.

## Data availability

The manuscript's S1–S4 files and the versioned finite-element reference materials are available at the paths above. Use a release or commit-specific repository URL when citing this deposit. No DOI is asserted by this repository.

