# Data provenance and file map

## Manuscript source

- Workspace file: `output/PLOS_ONE_final.docx`
- Title: Reinforcement learning for straightening stroke prediction under unloaded geometry constraints
- SHA-256: `8531d24f18558dff9885d43321e797888bcd1ff111f3bf129d908063536a9ae6`
- The DOCX is identified for provenance and is not included in this data/code repository.

## Supplementary archive records

The original author-prepared ZIP files are represented below. S1 is stored directly. Larger archives are split only at byte boundaries to fit the connected repository upload limit; `assemble_archives.py` joins their raw parts and verifies original byte size and SHA-256 before use.

- `supporting_information/S1_File.zip`: 1651723 bytes; SHA-256 `95b9f39dc3b48b48cf1ff4397d9aaaa3689ec4987c127bedf6b1aa58a2580346`; storage `single_file`.
- `supporting_information/S2_File.zip`: 3838786 bytes; SHA-256 `8a08ea9d82d9a63af23fdc8eec49564f4ffccb9771c729de9a5d14c58fc01fd5`; storage `numbered_binary_parts`.
  Parts: `part-001.bin` (1500000 bytes), `part-002.bin` (1500000 bytes), `part-003.bin` (838786 bytes).
- `supporting_information/S3_File.zip`: 7944643 bytes; SHA-256 `8eff44f890897a56c33ca78a218789cc94f63c4553a21541d3243dc0b0349617`; storage `numbered_binary_parts`.
  Parts: `part-001.bin` (1500000 bytes), `part-002.bin` (1500000 bytes), `part-003.bin` (1500000 bytes), `part-004.bin` (1500000 bytes), `part-005.bin` (1500000 bytes), `part-006.bin` (444643 bytes).
- `supporting_information/S4_File.zip`: 7966161 bytes; SHA-256 `2f022cff375085a5701bbec6978c809e12887c9b0ac78427196933d00e118a69`; storage `numbered_binary_parts`.
  Parts: `part-001.bin` (1500000 bytes), `part-002.bin` (1500000 bytes), `part-003.bin` (1500000 bytes), `part-004.bin` (1500000 bytes), `part-005.bin` (1500000 bytes), `part-006.bin` (466161 bytes).
- `engineering/Supplementary_Software_1.zip`: 5042308 bytes; SHA-256 `4df56b96fd2aa0d03383b03c5312661bae4b3c4f5c8f1b6edab37fed694c1253`; storage `numbered_binary_parts`.
  Parts: `part-001.bin` (1500000 bytes), `part-002.bin` (1500000 bytes), `part-003.bin` (1500000 bytes), `part-004.bin` (542308 bytes).

## Reference 32 mirror

The `engineering/` release is from `dengchuanlong/straightening`, commit `0960d0fcbf32a5824725853d7d381f7feeeeb22d`. All non-ZIP files are byte-for-byte Git-object matches to the cited commit. The original `Supplementary_Software_1.zip` is stored as raw-byte parts under `engineering/Supplementary_Software_1.zip.parts/`; `assemble_archives.py` reassembles it and verifies the SHA-256 recorded in the source `.sha256` file.

The third-party OPARA-288 attribution and CC BY-NC 4.0 terms remain in the mirrored notice and metadata. No broader licence is assigned.

## Limits

Large ANSYS result/restart binaries and full integration-point fields are not present in the compact packages. Their omission is recorded in the paper and package manifests. The mirror does not add missing checkpoints or grant additional rights.
