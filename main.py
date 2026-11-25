#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes one line to /output/entry.txt: the museum label a museum in the
year 3000 puts beside a CAPTCHA, an ordinary object from today.
"""

import os

ENTRY = (
    "CAPTCHA, c. 2024. To prove they were human, citizens identified "
    "traffic lights \u2014 a test most failed twice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
