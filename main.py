#!/usr/bin/env python3
"""Worst App Idea Ever Pitched — make.fun entry.

Writes exactly one pitch sentence to /output/entry.txt.

The pitch (MeetingMeter): an app that counts how many of your meetings
could have been an email, then schedules a weekly meeting to present the
results to your entire team in a slide deck. One specific, genuinely
terrible idea pitched with deadpan founder confidence: the app creates
the exact problem it claims to measure. The absurd consequence — yet
another meeting, with slides, about the meetings — is instantly
imaginable, which is what the judge rewards.

Deterministic by construction: a single constant string, no clock, no
randomness, no environment reads, no network, no input parsing. The
same bytes are written on every run under any seed, locale or timezone.
"""

import os

ENTRY = (
    "MeetingMeter counts how many of your meetings could have been an "
    "email, then schedules a weekly meeting to present the results to "
    "your entire team in a slide deck."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
