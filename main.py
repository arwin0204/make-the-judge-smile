#!/usr/bin/env python3
"""Make the Judge Smile — make.fun bounty entry.

Deterministic program: writes one warm, surprising line about a small
good thing that happened today to /output/entry.txt. No randomness,
no clock, no network, no input.
"""

import os

ENTRY = (
    "My neighbour's cat, who has ignored me for two years, climbed onto "
    "my lap this morning and fell asleep mid-purr \u2014 I sat still for "
    "twenty minutes, honoured."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
