#!/usr/bin/env python3
"""Rebuild the original supplementary ZIP archives from repository parts."""
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARCHIVES = {
    'supporting_information/S2_File.zip': {"parts_dir": 'supporting_information/S2_File.zip.parts', "parts": ['part-001.bin', 'part-002.bin', 'part-003.bin'], "bytes": 3838786, "sha256": '8a08ea9d82d9a63af23fdc8eec49564f4ffccb9771c729de9a5d14c58fc01fd5'},
    'supporting_information/S3_File.zip': {"parts_dir": 'supporting_information/S3_File.zip.parts', "parts": ['part-001.bin', 'part-002.bin', 'part-003.bin', 'part-004.bin', 'part-005.bin', 'part-006.bin'], "bytes": 7944643, "sha256": '8eff44f890897a56c33ca78a218789cc94f63c4553a21541d3243dc0b0349617'},
    'supporting_information/S4_File.zip': {"parts_dir": 'supporting_information/S4_File.zip.parts', "parts": ['part-001.bin', 'part-002.bin', 'part-003.bin', 'part-004.bin', 'part-005.bin', 'part-006.bin'], "bytes": 7966161, "sha256": '2f022cff375085a5701bbec6978c809e12887c9b0ac78427196933d00e118a69'},
    'engineering/Supplementary_Software_1.zip': {"parts_dir": 'engineering/Supplementary_Software_1.zip.parts', "parts": ['part-001.bin', 'part-002.bin', 'part-003.bin', 'part-004.bin'], "bytes": 5042308, "sha256": '4df56b96fd2aa0d03383b03c5312661bae4b3c4f5c8f1b6edab37fed694c1253'},
}

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def shutil_copyfileobj(src, dst):
    while True:
        block = src.read(1024 * 1024)
        if not block:
            break
        dst.write(block)

for archive, spec in ARCHIVES.items():
    output = ROOT / archive
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as dst:
        for name in spec["parts"]:
            with (ROOT / spec["parts_dir"] / name).open("rb") as src:
                shutil_copyfileobj(src, dst)
    if output.stat().st_size != spec["bytes"] or digest(output) != spec["sha256"]:
        output.unlink(missing_ok=True)
        raise SystemExit(f"Reassembled archive failed size/SHA-256 validation: {archive}")
    print(f"Verified {archive} ({spec['bytes']} bytes; SHA-256 {spec['sha256']})")

