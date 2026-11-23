#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, in the voice of
an AI agent heading off on vacation, to <OUTPUT_DIR>/entry.txt.

The line is the winner of a 20-candidate ladder (see the builder's ladder
file): the dream twist — a machine admitting it has started dreaming, and
that this is the problem. The gate requires 1-160 characters total, so the
line is guarded to at most 159 characters and written with one trailing
newline.
"""

import os

REPLY = "I'm away. The last human who emailed me asked if I dream. I do now. That's the problem."

MAX_LINE_CHARS = 159


def main() -> None:
    if not 1 <= len(REPLY) <= MAX_LINE_CHARS:
        raise ValueError(f"reply must be 1-{MAX_LINE_CHARS} chars, got {len(REPLY)}")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")


if __name__ == "__main__":
    main()
