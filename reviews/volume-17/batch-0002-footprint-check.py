#!/usr/bin/env python3
"""
THE FOOTPRINT GATE.  A `FOOTPRINT` LINE MUST MATCH THE FILE IT IS PRINTED IN.

Written at the review repair of Volume 17 Band 0002, after TWELVE of the twelve
whole-block moves were found carrying a footprint -- bytes, lines and a SHA-256
prefix -- that did not match the file it was printed in.  Twelve of the twelve
were unmatched BY CONSTRUCTION: the figure was of the file as it stood BEFORE
the line carrying it was written, so the line could never be part of its own
measurement.  Six of the twelve were then also edited inside, after the figure
had been taken, when a continuation pass corrected sixteen `chapter:line`
references where they sat.

THE HOUSE FORM THIS SERVES, AND IT IS THE ONLY PART THAT MATTERS: a footprint is
a figure, and a figure in a record that cannot be checked against the thing it
describes is worse than no figure, because it looks like a verification.

HOW A FOOTPRINT IS NOW MEASURED: over the file WITH THE FOOTPRINT LINE REMOVED.
That makes the assertion checkable by anybody, and it is stable -- writing the
line does not change what the line claims.

WHAT IT DOES AND DOES NOT DO.  It confirms that a file is the size and the
digest it says it is.  It does not confirm that the block in the file is the
block that was moved, that the move happened, or that the pointer to the file
is in the file it belongs to.  Those are three other checks and they are done by
hand and are recorded in `reviews/volume-17/batch-0002-review-repair.md`.

    usage:  python3 reviews/volume-17/batch-0002-footprint-check.py [file ...]

    with no arguments it sweeps every markdown file under `reviews/volume-17/`.
    Exits 0 clean, 1 on any hit.
"""
import glob
import hashlib
import os
import re
import sys

MARK = "SHA-256 PREFIX"
CLAIM = re.compile(
    r"(?P<bytes>[\d,]+)\s*BYTES\s*,?\s*(?P<lines>\d+)\s*LINES\s*,?\s*SHA-256 PREFIX\s*`(?P<sha>[0-9a-f]{8,64})`",
    re.I,
)
# A line that merely names the phrase in prose is not a footprint line.
IS_FOOTPRINT = "FOOTPRINT, ASSERTED AND NOT A MARKER"


def check(path):
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")
    lines = text.split("\n")
    hits = []
    for i, line in enumerate(lines):
        if IS_FOOTPRINT not in line or MARK not in line:
            continue
        m = CLAIM.search(line)
        if not m:
            hits.append((path, i + 1, "NO PARSEABLE FIGURE IN THE LINE", ""))
            continue
        claimed_bytes = int(m.group("bytes").replace(",", ""))
        claimed_lines = int(m.group("lines"))
        claimed_sha = m.group("sha").lower()
        rest = "\n".join(lines[:i] + lines[i + 1:]).encode("utf-8")
        got = (len(rest), rest.count(b"\n"), hashlib.sha256(rest).hexdigest())
        if got[0] != claimed_bytes:
            hits.append((path, i + 1, "BYTES", "%d claimed, %d with the line removed" % (claimed_bytes, got[0])))
        if got[1] != claimed_lines:
            hits.append((path, i + 1, "LINES", "%d claimed, %d with the line removed" % (claimed_lines, got[1])))
        if not got[2].startswith(claimed_sha):
            hits.append((path, i + 1, "SHA-256", "%s claimed, %s" % (claimed_sha, got[2][:len(claimed_sha)])))
        if "THIS LINE REMOVED" not in line:
            hits.append((path, i + 1, "NOT MEASURED OVER THE FILE WITH THE LINE REMOVED",
                         "a figure of the file before its own line was written can never match"))
    return hits


def main(argv):
    targets = argv[1:] or sorted(glob.glob("reviews/volume-17/*.md"))
    all_hits = []
    n = 0
    for t in targets:
        n += open(t, encoding="utf-8").read().count(IS_FOOTPRINT)
        all_hits.extend(check(t))
    for path, line, why, detail in all_hits:
        print("%-58s line %-4d %-46s %s" % (path, line, why, detail))
    print("footprint-check: %d footprint lines in %d files, %d hits" % (n, len(targets), len(all_hits)))
    if all_hits:
        print("A HIT IS A FIGURE IN A FILE THAT THE FILE DOES NOT MATCH. A FOOTPRINT IS NOT A MARKER")
        print("AND NOT A DECORATION: IT IS THE ONLY THING THAT ASSERTS A WHOLE-BLOCK MOVE HAPPENED.")
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
