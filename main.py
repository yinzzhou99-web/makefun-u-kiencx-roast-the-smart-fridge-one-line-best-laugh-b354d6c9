#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (1-160 chars) to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

LINE = (
    "My smart fridge keeps a photo log of everything I eat, so somewhere "
    "in the cloud there's a timelapse of me, alone, eating pickles over "
    "the sink at 1 a.m."
)


def main() -> None:
    text = LINE.strip()
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the line and nothing else.
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
