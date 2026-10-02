#!/usr/bin/env python3
"""
THE MISSING EIGHTH GATE.  A `chapter:line` REFERENCE MUST LAND ON A LINE OF TEXT.

Copied out of `reviews/volume-18/batch-0003-lineref-check.py` and RE-POINTED TO
VOLUME 19, at the review repair of Volume 19 Band 0001, for ONE REASON AND THE
REASON IS PRINTED BESIDE THE CALIBRATION IN THE RECEIPT:

THE RECEIPT FOR `901`-`910` PRINTED **1,114 REFERENCES IN 84 FILES, 6 HITS, AND
NOT ONE IS IN A FILE THIS BAND WROTE**, AND THAT FIGURE WAS A FIGURE OF THE
SCOPE AND NOT OF THE THING.  THE SCRIPT IT NAMED STILL READS `VOLUMES = 18` AND
STILL FILTERS ON `/volume-18/` ONLY, SO IT OPENED `state/` AND VOLUME 18 AND
NEVER OPENED ONE LINE OF `reviews/volume-19/`.  A GATE THAT CANNOT SEE THE FILES
A PASS WROTE IS A GATE THAT HAS NEVER CHECKED THEM, AND THAT HAS NOW BEEN TRUE
OF EVERY REVIEW IN THIS REPOSITORY.

WHAT IT DOES AND DOES NOT DO.  It opens the named chapter, splits it on newlines,
and checks that the named line index exists and is not empty.  That is ALL.  It
does not read the line.  It cannot tell whether the line says what the citing
file claims it says -- and on this band's own blocks it could not have: it found
ELEVEN REFERENCES PAST THE END OF THE CHAPTER THEY NAME, and BEHIND THOSE
ELEVEN THERE WAS ONE CLAIM WITH NOTHING ON THE PAGE BEHIND IT AT ALL.  A
reference that lands on a line of text and points at the wrong sentence passes
here and is wrong, and that is stated because a gate that cannot see a class of
figure is not a gate on that class.

    usage:  python3 reviews/volume-19/batch-0003-lineref-check.py [file ...]

    with no arguments it sweeps every state file, every volume-19 review file
    and every volume-19 batch prompt.  Exits 0 clean, 1 on any hit.

THE HOUSE FORM THIS EXISTS TO SERVE: a figure in a state file is a claim about
a chapter and not a fact about one, and a line reference is the cheapest figure
in the repository to copy and the most expensive to get wrong, because it looks
like a verification.
"""
import os
import re
import sys

REF = re.compile(r"`(\d{3,4}):(\d+)`")

VOLUMES = 19


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
