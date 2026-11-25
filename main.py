#!/usr/bin/env python3
"""One Star for Monday.

Writes a single-line, one-star restaurant review of Monday
to /output/entry.txt. The review reads like a real diner's
complaint: a bad table, a cold dish, and an unfair bill, with
the joke landing on Monday itself.
"""

import os

# The review: Monday as a restaurant. The table is the worst seat
# in the house (by the alarm clock), the dish is the weekend served
# cold, and the bill charges a full week for one bad morning.
# Twenty words, one line, plain text, payoff first.
REVIEW = (
    "One star. Monday seated us by the alarm clock, served the "
    "weekend cold, and billed us for the whole week."
)


def main() -> None:
    text = REVIEW.strip()
    words = text.split()
    # Gate: 1-180 characters, at most 25 words, single line.
    assert 1 <= len(text) <= 180, f"length {len(text)} out of range"
    assert len(words) <= 25, f"word count {len(words)} over 25"
    assert "\n" not in text and "\r" not in text, "must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back and compare byte for byte: the file on disk must
    # be exactly the reviewed text, with no trailing newline added.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt differs from the review"
    assert not written.endswith("\n"), "no trailing newline allowed"
    print(f"wrote {len(written)} chars, {len(words)} words")


if __name__ == "__main__":
    main()
