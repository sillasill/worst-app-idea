#!/usr/bin/env python3
"""Worst-app pitch for make.fun: a single sentence, at most 240 characters.

The program writes the pitch to /output/entry.txt (or to the directory named
by MAKEFUN_OUTPUT_DIR, which exists only so the entry can be run and checked
on a machine where /output is not writable). The pitch itself is fixed text:
no randomness, no clock, no network, standard library only.
"""

import os
from pathlib import Path

PITCH = (
    "LeafScore is the app that lets your houseplants rate your care on a "
    "five-star scale and publish scathing public reviews, so busy plant "
    "parents can finally discover what their fern really thinks of the "
    "three weeks they forgot it existed."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-240")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
