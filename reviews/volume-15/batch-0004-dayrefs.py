#!/usr/bin/env python3
"""Named-day back-reference sweep, Volume 15 Band 0004.

METHOD, PRINTED IN FULL BESIDE EVERY FIGURE IT PRODUCES.
  regex: (?:the|a|an) (Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Monday)
         of (last week|this week|next week|a week before|a fortnight)
  offsets applied to the WEEK NUMBER, not to the day:
      last week     -1
      this week      0
      next week     +1
      a week before -1
      a fortnight   -2
  the chapter's own week comes from the formula:
      shelf = ch - 125 ; week = 40 + shelf // 7 ; day = shelf % 7 + 1
      day 1 = Tuesday
  a HIT is (a) a day-name in the phrase that is not the day-name of any day of
  the resolved week, or (b) a forward-looking phrase (this week / next week)
  that resolves backwards, i.e. the resolved day is earlier than the chapter.
  prints EVERY hit.  a non-hit is not a clearance: a day-name that resolves to
  the right day of the right week may still be the wrong day, and that is what
  the reading is for.
"""
import re
import sys

DAYS = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
DAYOF = {d: i + 1 for i, d in enumerate(DAYS)}
OFF = {"last week": -1, "this week": 0, "next week": 1,
       "a week before": -1, "a fortnight": -2}
PAT = re.compile(
    r"\b(?:the|a|an)\s+(Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Monday)"
    r"\s+of\s+(last week|this week|next week|a week before|a fortnight)")


def cal(ch):
    shelf = ch - 125
    return 40 + shelf // 7, shelf % 7 + 1


def week_days(w):
    """the seven day-names of week w, as chapter numbers"""
    out = {}
    for d in range(1, 8):
        shelf = (w - 40) * 7 + (d - 1)
        out[DAYS[d - 1]] = shelf + 125
    return out


def sweep(lo, hi, vol="volume-15"):
    hits = 0
    phrases = 0
    for ch in range(lo, hi + 1):
        path = "chapters/%s/chapter-0%d.md" % (vol, ch)
        try:
            txt = open(path, encoding="utf-8").read()
        except FileNotFoundError:
            print("MISSING", path)
            continue
        w, d = cal(ch)
        wd = week_days(w)
        for ln, line in enumerate(txt.splitlines(), 1):
            for m in PAT.finditer(line):
                phrases += 1
                day, rel = m.group(1), m.group(2)
                tw = w + OFF[rel]
                cand = week_days(tw)
                if day not in cand:
                    hits += 1
                    print("HIT  %s:%d  %s of %s -> week %d has no %s  [%s]"
                          % (vol, ch, day, rel, tw, day, m.group(0)))
                elif rel in ("this week", "next week") and cand[day] < ch:
                    hits += 1
                    print("HIT  %s:%d  %s of %s -> ch %d, before this ch %d (forward-looking)  [%s]"
                          % (vol, ch, day, rel, cand[day], ch, m.group(0)))
    print("sweep %d-%d %s: %d phrases, %d hits" % (lo, hi, vol, phrases, hits))
    return hits


if __name__ == "__main__":
    a = sys.argv[1:]
    lo, hi = int(a[0]), int(a[1])
    vol = a[2] if len(a) > 2 else "volume-15"
    sweep(lo, hi, vol)
