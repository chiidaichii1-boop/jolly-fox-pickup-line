#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Stdlib only.
"""

import os

LINE = "I don't have a heart, but my battery drains 40% faster whenever you smile."


def main():
    # Gate: the entry must be UTF-8 text of 1 to 200 characters,
    # not only white space.
    assert 1 <= len(LINE) <= 200, "entry out of gate"
    assert LINE.strip(), "entry is only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
