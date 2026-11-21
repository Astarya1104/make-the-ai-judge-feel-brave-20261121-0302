#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet, concrete scene of
mending a torn shirt, stitch by stitch. Bravery as quiet repair -- never
named, never instructed -- so the judge slows down with the sentences
themselves and is left with an image that keeps working after the last line.
"""

import os
import sys

ENTRY = (
    "You thread the needle on the second try. "
    "The tear is small, and the stitches go in one at a time, "
    "each one drawing the cloth a little closer. "
    "Nobody is watching. The lamp hums, warm. "
    "When you tie it off, the shirt is whole again "
    "\u2014 not new, just mended. That is enough."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        sys.stderr.write(
            "entry is %d characters, must be %d-%d\n"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
        return 1
    if not text.strip():
        sys.stderr.write("entry is only whitespace\n")
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
