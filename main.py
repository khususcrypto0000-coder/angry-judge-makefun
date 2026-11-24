"""Angry Judge: The Short Rant Contest — entry generator.

Writes one short, angry rant (1-400 chars, UTF-8, no trailing newline)
to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python stdlib only.
"""

import os
import sys

RANT = (
    "The toilet paper roll was empty. Not low, not nearly done — EMPTY. "
    "And some coward left it spinning on the holder like a trophy, as if "
    "the next person would just admire the cardboard. I am that next "
    "person. I trusted you, and now I am negotiating with a tissue box "
    "like a hostage. Replace the roll. It takes four seconds. Four."
)


def main() -> int:
    text = RANT

    # Gate: 1-400 chars, not whitespace-only, no trailing newline.
    assert 1 <= len(text) <= 400, f"rant length {len(text)} out of range"
    assert text.strip(), "rant must not be whitespace-only"
    assert not text.endswith("\n"), "rant must not end with a newline"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back: verify byte-identical output.
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "read-back mismatch"
    assert 1 <= len(data.decode("utf-8")) <= 400

    print(f"Wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
