#!/usr/bin/env python3
"""Off-Key Angels.

One line of famous last words for the make.fun epitaph bounty: the
dying man hears the angels singing, and they are off-key. This program
leaves exactly that line in /output/entry.txt, with no trailing
newline, after proving it passes the competition gate.
"""

import os
import sys
import unicodedata

LINE = "I can hear the angels singing. They're off-key."
DEST = "/output/entry.txt"
CAP = 150


def _is_blank(t):
    return t.strip() == ""


def _too_long(t):
    return len(t) > CAP


def _split(t):
    return "\n" in t or "\r" in t


def _padded(t):
    return t.strip() != t


def _has_hidden(t):
    for ch in t:
        if unicodedata.category(ch) == "Cf":
            return True
        if ord(ch) < 32 or ord(ch) == 127:
            return True
    return False


RULES = (
    (_is_blank, "blank"),
    (_too_long, "too long"),
    (_split, "line break"),
    (_padded, "edge whitespace"),
    (_has_hidden, "hidden character"),
)


def faults(text):
    """Every gate violation in `text`; an empty list means it passes."""
    return [name for fn, name in RULES if fn(text)]


def save():
    """Write LINE to DEST, then prove the bytes on disk match LINE."""
    problems = faults(LINE)
    if problems:
        raise SystemExit("entry fails the gate: " + "; ".join(problems))
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(DEST, "rb") as handle:
        raw = handle.read()
    if raw != LINE.encode("utf-8"):
        raise SystemExit("read-back mismatch: disk differs from LINE")


def _check_cases():
    """Run the gate over known good and bad inputs; return the bad count."""
    cases = {
        "empty": ("", False),
        "spaces only": ("   ", False),
        "151 chars": ("x" * 151, False),
        "two lines": ("two\nlines", False),
        "carriage return": ("carriage\rreturn", False),
        "leading space": (" leading", False),
        "trailing space": ("trailing ", False),
        "bell": ("\x07bell", False),
        "tab inside": ("a\tb", False),
        "DEL inside": ("a\x7fb", False),
        "zero-width only": ("\u200b", False),
        "zero-width inside": ("\u200bhello", False),
        "one char": ("a", True),
        "150 chars": ("x" * 150, True),
        "the entry": (LINE, True),
    }
    bad = 0
    for name, (text, want) in cases.items():
        got = faults(text) == []
        if got != want:
            bad += 1
            print("FAIL %s: wanted %s, got %s" % (name, want, got))
    return bad


def _self_test():
    bad = _check_cases()
    save()
    with open(DEST, "rb") as handle:
        raw = handle.read()
    if raw != LINE.encode("utf-8"):
        print("FAIL: file on disk is not the entry")
        bad += 1
    elif faults(raw.decode("utf-8")):
        print("FAIL: file on disk fails the gate")
        bad += 1
    print(
        "self-test: %d bad of %d cases; entry is %d chars / %d bytes"
        % (bad, 15, len(LINE), len(LINE.encode("utf-8")))
    )
    return 1 if bad else 0


def _run(argv):
    if "--self-test" in argv:
        return _self_test()
    save()
    return 0


if __name__ == "__main__":
    sys.exit(_run(sys.argv[1:]))
