#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

Writes a single joke (at most 200 characters) to /output/entry.txt.
Uses only the Python standard library.
"""

import os
from pathlib import Path

JOKE = (
    "Monday morning, my toaster filed for emotional damages, the lamp "
    "testified, and I was sentenced to a second Monday as an adult."
)
# Picked from 10 candidates (see CANDIDATES.md): the absurdist courtroom
# escalation is the most surprising, its kicker is a real punchline, and it
# uses none of the tired Monday cliches (alarm, coffee, snooze, bed).


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    # Read back and confirm the file holds exactly the joke, no extra
    # whitespace or newline, so the gate sees 1-200 clean characters.
    written = out.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written file does not match the joke exactly")
    print(f"Wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
