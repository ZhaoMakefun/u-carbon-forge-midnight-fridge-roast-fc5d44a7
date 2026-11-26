#!/usr/bin/env python3
"""Midnight roast for a fridge with a curfew.

At midnight the appliance turns bouncer: doors locked, yet
still happy to lecture its owner about their choices from
behind a door it refuses to open. The lines below check
that roast and store it as entry.txt.
"""

import sys
from os import getenv
from pathlib import Path

TEXT = "My smart fridge locks itself at midnight like a bouncer, then lectures me about my choices through a door it will not even open."
MAX_LEN = 200


def final_text():
    value = TEXT.strip()
    if value == "":
        raise SystemExit("no roast to write — the text came out blank")
    if len(value) > MAX_LEN:
        raise SystemExit(f"roast is {len(value)} characters, over the {MAX_LEN} limit")
    if set(value) & {"\n", "\r"}:
        raise SystemExit("roast must be one line — no line breaks allowed")
    value.encode("utf-8")
    return value


destination = Path(getenv("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(final_text(), encoding="utf-8")
