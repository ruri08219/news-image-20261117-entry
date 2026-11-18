#!/usr/bin/env python3
"""news-image-20261117 entry: write the front-page image to /output/entry.png.

The image is bundled as entry.jpg next to this file. This script copies it
byte-for-byte to /output/entry.png, verifying the SHA-256 digest and byte
size before and after the copy, and failing loudly on any mismatch.
No network, no clock, no randomness: repeated runs produce identical bytes.
"""

import hashlib
import os
import sys

ENTRY_SHA256 = "97ca4146e85eb61c9ac5c538c070b4db1ed0b20d37b71caffae97d64877f9cdb"
ENTRY_SIZE = 267804
ENTRY_NAME = "entry.jpg"
OUTPUT_PATH = "/output/entry.png"


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)

    if not os.path.isfile(src):
        print(f"ERROR: bundled image not found: {src}", file=sys.stderr)
        return 1

    with open(src, "rb") as f:
        data = f.read()

    if len(data) != ENTRY_SIZE:
        print(f"ERROR: {ENTRY_NAME} size {len(data)} != expected {ENTRY_SIZE}",
              file=sys.stderr)
        return 1
    if sha256_hex(data) != ENTRY_SHA256:
        print(f"ERROR: {ENTRY_NAME} sha256 mismatch", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("ERROR: output bytes differ from bundled image", file=sys.stderr)
        return 1
    if len(written) != ENTRY_SIZE or sha256_hex(written) != ENTRY_SHA256:
        print("ERROR: output verification failed", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(written)} bytes, sha256 {ENTRY_SHA256})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
