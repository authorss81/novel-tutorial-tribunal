#!/usr/bin/env python3
"""Weekday detector preserved for volume-21 close section 2.2. Read-only.

Written during the review repair of close-0006 because section 2.2 of
reviews/volume-21/volume-21-close.md carried four volumes of figures with no
instrument behind them, so nobody could check them. Every rule below is stated
here in full and every figure printed in section 2.2 is the output of this file.

    ANCHORED  a weekday immediately followed by
                "of the hundred and <ordinal> week" | "of that week" | "of this week"
              counts occurrences, whole file, title line included.

    BARE      a weekday preceded by since | on | that | last, an optional
              article, NOT preceded by "of " and NOT followed by " of".
              This is the rule section 2.2 states in words.

    LOOSE     a paragraph-window detector: every weekday token standing in a
              paragraph that does not contain "of the hundred and". Printed only
              so that nobody compares it with BARE.

    GATE      git diff --numstat over chapters/volume-21/, so the claim in
              section 3 about what moved can be checked instead of believed.

Run:  python3 reviews/volume-21/volume-21-close-weekdays-0V21L.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DAYS = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"

ANCHORED = re.compile(
    r"(?:%s)\s+of\s+(?:the\s+hundred\s+and\s+[A-Za-z\-]+|that|this)\s+week" % DAYS)
BARE = re.compile(
    r"(?<!of )\b(?:since|on|that|last)(?:\s+(?:a|an|the))?\s+(?:%s)\b(?!\s+of)" % DAYS)
DAYTOK = re.compile(r"\b(?:%s)\b" % DAYS)

VOLUMES = [(851, 900, 18), (901, 950, 19), (951, 1000, 20), (1001, 1050, 21)]


def vol_dir(lo):
    return os.path.join(ROOT, "chapters", "volume-%02d" % ((lo - 1) // 50 + 1))


def path(lo, ch):
    return os.path.join(vol_dir(lo), "chapter-%04d.md" % ch)


def whole(lo, ch):
    with open(path(lo, ch), encoding="utf-8") as fh:
        return fh.read()


def body(lo, ch):
    return "\n".join(whole(lo, ch).split("\n")[1:])


def main():
    print("=" * 78)
    print("A. ANCHORED — weekday + 'of the hundred and <ord> week' | 'of that week'")
    print("   | 'of this week'.  Whole file, title line included.")
    print("=" * 78)
    for lo, hi, label in VOLUMES:
        total, chapters = 0, set()
        for ch in range(lo, hi + 1):
            hits = ANCHORED.findall(whole(lo, ch))
            if hits:
                total += len(hits)
                chapters.add(ch)
        print("  volume %-2d  %4d-%4d  anchored = %4d   in %2d chapters"
              % (label, lo, hi, total, len(chapters)))

    print()
    print("=" * 78)
    print("B. BARE — since/on/that/last + optional article + weekday, no 'of'")
    print("   before it and no 'of' after it.  Body only.")
    print("=" * 78)
    per = {}
    for lo, hi, label in VOLUMES:
        total, chapters = 0, set()
        for ch in range(lo, hi + 1):
            hits = [m.group(0) for m in BARE.finditer(body(lo, ch))]
            if hits:
                total += len(hits)
                chapters.add(ch)
                per[ch] = hits
        print("  volume %-2d  %4d-%4d  bare     = %4d   in %2d chapters"
              % (label, lo, hi, total, len(chapters)))

    print()
    print("  volume 21, chapter by chapter, and the phrase in each:")
    for ch in range(1001, 1051):
        if ch in per:
            print("    %d  %2d  %s" % (ch, len(per[ch]), "; ".join(per[ch])))

    print()
    print("=" * 78)
    print("C. LOOSE — paragraph window.  Every weekday token in a paragraph that")
    print("   does not contain 'of the hundred and'.  A DIFFERENT FIGURE ON A")
    print("   DIFFERENT BASIS.  Do not compare it with B.")
    print("=" * 78)
    for lo, hi, label in VOLUMES:
        total = 0
        for ch in range(lo, hi + 1):
            for para in re.split(r"\n\s*\n", body(lo, ch)):
                if "of the hundred and" not in para:
                    total += len(DAYTOK.findall(para))
        print("  volume %-2d  %4d-%4d  loose    = %4d" % (label, lo, hi, total))

    print()
    print("=" * 78)
    print("D. GATE — what actually moved in chapters/volume-21/ in the close commit")
    print("=" * 78)
    base, head = (sys.argv[1:3] + ["HEAD~1", "HEAD"])[:2]
    try:
        shown = subprocess.run(
            ["git", "rev-parse", "--short", base],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
        shown += subprocess.run(
            ["git", "rev-parse", "--short", head],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
        out = subprocess.run(
            ["git", "diff", "-U0", base, head, "--", "chapters/volume-21/"],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except Exception as exc:                                  # pragma: no cover
        print("  git unavailable here (%s); run this from a checkout to check it."
              % exc)
        return 0
    print("  diffing %s..%s   (pass two commit-ish arguments to point it elsewhere)"
          % (shown[0], shown[1]))

    title_lines, body_lines, current = {}, {}, None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = os.path.basename(line[6:])
            title_lines.setdefault(current, [])
            body_lines.setdefault(current, [])
        elif line.startswith("@@"):
            new = line.split("+")[1].split(" ")[0]
            start, _, count = new.partition(",")
            start, count = int(start), int(count or 1)
            for n in range(start, start + count):
                (title_lines if n == 1 else body_lines)[current].append(n)

    title_only = sorted(c for c in title_lines if title_lines[c] and not body_lines[c])
    with_body = sorted(c for c in body_lines if body_lines[c])
    print("  chapters touched at all: %d" % len(title_lines))
    print("  of those, title line ONLY: %d" % len(title_only))
    for name in with_body:
        print("  of those, body lines too: %s at line(s) %s"
              % (name, ", ".join(str(n) for n in body_lines[name])))
    print()
    print("  READ IT AS: a title line changed in %d chapters. A body line changed"
          % len(title_lines))
    print("  in %d chapter and in no other. 'body-changed chapters: NONE' is FALSE,"
          % len(with_body))
    print("  and section 3 of the close now prints the true gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
