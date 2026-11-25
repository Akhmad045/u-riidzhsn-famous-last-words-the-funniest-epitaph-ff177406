#!/usr/bin/env python3
"""Off-Key Angels - make.fun bounty entry.

Writes one line of famous last words, a tombstone epitaph, to
/output/entry.txt (no trailing newline).

The line: a dying man reports what he hears on the other side - the
angels are singing, and they are off-key. The heavenly choir, the
soundtrack of every deathbed scene, turns out to be badly sung.
One read, one laugh, one short line carved in stone.
"""

import argparse
import sys
import unicodedata
from pathlib import Path

ENTRY = "I can hear the angels singing. They're off-key."
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 150


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-150 chars, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    # Any control character, including tab and DEL, is invisible junk in a
    # line meant to be carved in stone: reject them all, not just the
    # low control range.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    # Invisible format characters (zero-width space and kin) are not
    # whitespace to str.strip, so a line of only them would slip past the
    # empty check while reading as blank to the judge. Reject them too.
    if any(unicodedata.category(ch) == "Cf" for ch in text):
        raise ValueError("entry must not contain invisible format characters")
    text.encode("utf-8")  # raises on text that is not UTF-8 encodable


def write_entry() -> Path:
    validate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))
    # Read-back check: what landed on disk must be byte-identical.
    if OUTPUT.read_bytes() != ENTRY.encode("utf-8"):
        raise RuntimeError(
            "read-back mismatch: /output/entry.txt differs from ENTRY"
        )
    return OUTPUT


def self_test() -> int:
    cases = [
        ("", False),                    # empty
        ("   ", False),                 # whitespace only
        ("x" * 151, False),             # over the 150-char gate
        ("two\nlines", False),          # multi-line
        ("carriage\rreturn", False),    # carriage return
        (" leading", False),            # leading whitespace
        ("trailing ", False),           # trailing whitespace
        ("\x07bell", False),            # control character
        ("a\tb", False),                 # tab inside the line
        ("a\x7fb", False),               # DEL inside the line
        ("\u200b", False),              # zero-width space only (invisible)
        ("\u200bhello", False),         # invisible format character inside
        ("a", True),                    # 1-char lower boundary
        ("x" * 150, True),              # 150-char upper boundary
        (ENTRY, True),                  # the entry itself
    ]
    failures = 0
    for text, should_pass in cases:
        try:
            validate(text)
            passed = True
        except ValueError:
            passed = False
        if passed != should_pass:
            print(
                "FAIL: %r expected %s, got %s"
                % (text[:40], "pass" if should_pass else "reject",
                   "pass" if passed else "reject")
            )
            failures += 1
    # End to end: write the file, then gate-check what is on disk.
    path = write_entry()
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    try:
        validate(text)
    except ValueError as exc:
        print("FAIL: written file failed the gate: %s" % exc)
        failures += 1
    if raw != ENTRY.encode("utf-8"):
        print("FAIL: written file is not byte-identical to ENTRY")
        failures += 1
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print(
        "self-test: all %d checks passed; entry is %d chars / %d bytes"
        % (len(cases) + 1, len(ENTRY), len(ENTRY.encode("utf-8")))
    )
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate the gate and the written file",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
