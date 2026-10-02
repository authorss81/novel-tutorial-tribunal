#!/usr/bin/env python3
"""
THE MISSING EIGHTH GATE.  A `chapter:line` REFERENCE MUST LAND ON A LINE OF TEXT.

Written at the continuation pass of Volume 17 Band 0002, after SIXTEEN
`chapter:line` references were found wrong in the Volume 17 review blocks --
including `801:81`, which named a man of forty-four's own mistake instead of
Orla Fennimore's retired counter at `802:170`, and `803:79`, which named a
blank line instead of the inversion of the volume's midpoint at `803:111`.

WHAT IT DOES AND DOES NOT DO.  It opens the named chapter, splits it on newlines,
and checks that the named line index exists and is not empty.  That is ALL.  It
does not read the line.  It cannot tell whether the line says what the citing
file claims it says -- the Orla finding was of that kind and was found by
reading, not by this script.  A reference that lands on a line of text and
points at the wrong sentence passes here and is wrong, and that is stated
because a gate that cannot see a class of figure is not a gate on that class.

    ⚠⚠ COPIED AND RE-POINTED TO VOLUME 18 AT THE REVIEW REPAIR OF BAND 0003,
    ⚠⚠ BECAUSE THE RECEIPT FOR `871`–`880` SAID IT HAD BEEN COPIED OUT AND
    ⚠⚠ RE-POINTED AND NO SUCH FILE WAS IN THE REPOSITORY TO BE COPIED. ⚠⚠ THE
    ⚠⚠ ORIGINAL HARD-CODES `VOLUMES = 18` AND HAS NEVER LOOKED AT ONE FILE OF
    ⚠⚠ VOLUME 18, ⚠⚠ SO ITS REPORTED FIGURE WAS A FIGURE OF THE SET IT HAPPENS
    ⚠⚠ TO SWEEP AND NOT OF THE SET IT NAMES. ⚠⚠ A GATE THAT CANNOT SEE THE
    ⚠⚠ FILES A PASS WROTE IS A GATE THAT HAS NEVER CHECKED THEM.

    usage:  python3 reviews/volume-18/batch-0003-lineref-check.py [file ...]

    with no arguments it sweeps every state file, every volume-17 review file
    and every volume-17 batch prompt.  Exits 0 clean, 1 on any hit.

THE HOUSE FORM THIS EXISTS TO SERVE: a figure in a state file is a claim about
a chapter and not a fact about one, and a line reference is the cheapest figure
in the repository to copy and the most expensive to get wrong, because it looks
like a verification.
"""
import os
import re
import sys

REF = re.compile(r"`(\d{3,4}):(\d+)`")

VOLUMES = 18


def build_map():
    """chapter number -> path, across every volume that is on disk."""
    m = {}
    root = "chapters"
    if not os.path.isdir(root):
        sys.exit("chapters/ is not here; run this from the repository root.")
    for vol in sorted(os.listdir(root)):
        d = os.path.join(root, vol)
        if not vol.startswith("volume-") or not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            hit = re.match(r"chapter-(\d+)\.md$", name)
            if hit:
                m[int(hit.group(1))] = os.path.join(d, name)
    return m


def default_targets():
    out = []
    for d in ("state", "reviews", "workspace"):
        if not os.path.isdir(d):
            continue
        for base, _dirs, files in os.walk(d):
            for name in sorted(files):
                if not name.endswith(".md"):
                    continue
                if name == "phase-ledger.json":
                    continue
                p = os.path.join(base, name)
                if "/volume-%02d/" % VOLUMES in p or base == "state":
                    out.append(p)
    return sorted(out)


def check(path, chapters, cache):
    text = open(path, encoding="utf-8").read()
    hits = []
    for m in REF.finditer(text):
        ch, ln = int(m.group(1)), int(m.group(2))
        if ch not in chapters:
            hits.append((path, m.start(), ch, ln, "NO SUCH CHAPTER"))
            continue
        if ch not in cache:
            cache[ch] = open(chapters[ch], encoding="utf-8").read().split("\n")
        lines = cache[ch]
        if ln < 1 or ln > len(lines):
            hits.append((path, m.start(), ch, ln, "PAST END OF FILE"))
        elif not lines[ln - 1].strip():
            hits.append((path, m.start(), ch, ln, "BLANK LINE"))
    return hits


def main(argv):
    chapters = build_map()
    targets = argv[1:] or default_targets()
    cache = {}
    total = 0
    all_hits = []
    for t in targets:
        total += len(REF.findall(open(t, encoding="utf-8").read()))
        all_hits.extend(check(t, chapters, cache))
    for path, _off, ch, ln, why in all_hits:
        print("%-52s %s:%-5d %s" % (path, ch, ln, why))
    print("lineref-check: %d references in %d files, %d hits" % (total, len(targets), len(all_hits)))
    if all_hits:
        print("A HIT IS A REFERENCE THAT DOES NOT LAND ON A LINE OF TEXT. IT IS NOT A JUDGEMENT")
        print("ABOUT WHAT THE LINE SAYS, AND A REFERENCE THAT LANDS ON THE WRONG SENTENCE")
        print("PASSES THIS SCRIPT AND IS WRONG. READ THE LINE.")
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
