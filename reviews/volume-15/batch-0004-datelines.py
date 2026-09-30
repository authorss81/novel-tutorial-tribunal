#!/usr/bin/env python3
"""Date-line verifier, Volume 15 Band 0004.

Recomputes every clock from the formula and checks the words printed in the
date line and the title against it.  A HIT is a figure or a day-name in the
date line or the title that is not what the formula gives.

  shelf = ch - 125 ; week = 40 + shelf // 7 ; day = shelf % 7 + 1 ; day 1 = Tuesday
  morning = ch - 250 ; settlement = ch - 400 ; fever = ch - 283 days
  hall = ch - 446 ; clear = ch - 500

THE CALIBRATION IS 701-720 AND IT MUST COME BACK CLEAN, BECAUSE A METHOD
THAT DOES NOT REPRODUCE ON ITS OWN CALIBRATION IS NOT A METHOD YET.
"""
import io
import re
import sys

DAYS = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
ORD = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ORDINAL = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
           7: "seventh", 8: "eighth", 9: "ninth"}


def two(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
    return str(n)


def words(n):
    if n < 100:
        return two(n)
    h, r = divmod(n, 100)
    return ONES[h] + " hundred" + (" and " + two(r) if r else "")


def ordinal_last(t):
    """'eighty-one' -> 'eighty-first', 'eighty' -> 'eightieth', 'twenty' -> 'twentieth'"""
    tens_ord = {"twenty": "twentieth", "thirty": "thirtieth", "forty": "fortieth",
                "fifty": "fiftieth", "sixty": "sixtieth", "seventy": "seventieth",
                "eighty": "eightieth", "ninety": "ninetieth"}
    if "-" in t:
        head, tail = t.split("-", 1)
        return head + "-" + ORDINAL[["one", "two", "three", "four", "five", "six",
                                     "seven", "eight", "nine"].index(tail) + 1]
    if t in tens_ord:
        return tens_ord[t]
    return ORDINAL[int(t)]


def weekword(w):
    h, r = divmod(w, 100)
    return "hundred" + (" and " + ordinal_last(two(r)) if r else "")


def check(ch, vol="volume-15"):
    path = "chapters/%s/chapter-0%d.md" % (vol, ch)
    lines = io.open(path, encoding="utf-8").read().splitlines()
    title, date = lines[0], lines[2]
    shelf = ch - 125
    week, day = 40 + shelf // 7, shelf % 7 + 1
    hits = []

    m = re.match(r"^(.*?) day of the (hundred(?: and [\w-]+)?) week\.", date)
    if not m:
        hits.append("date line: no week/day clause")
    else:
        first, wn = m.group(1).strip(), m.group(2)
        if wn != weekword(week):
            hits.append("week: %r != %r" % (wn, weekword(week)))
        got = 7 if first.startswith("Seventh and last") else (
            ORD.index(first) + 1 if first in ORD else -1)
        if got != day:
            hits.append("day ordinal: %r -> %s, formula %s" % (first, got, day))

    dn = re.findall(r"\b(" + "|".join(DAYS) + r")\b", title)
    if dn and dn[0] != DAYS[day - 1]:
        hits.append("title day-name: %r != %r" % (dn[0], DAYS[day - 1]))

    # the date lines print the morning with an ordinal on the last word:
    # 'His four hundred and eighty-first morning'
    m = re.search(r"His (.+?) morning\.", date)
    n = ch - 250
    exp = ordinal_last(two(n)) if n < 100 else \
        ONES[n // 100] + " hundred and " + ordinal_last(two(n % 100))
    if not m:
        hits.append("no morning clause")
    elif m.group(1) != exp:
        hits.append("morning: %r != %r" % (m.group(1), exp))

    for label, pat, tail in (
            ("settlement", r"Three hundred and ([\w-]+) days after the settlement\.", two(ch - 400 - 300)),
            ("hall", r"Two hundred and ([\w-]+) days since the division\.", two(ch - 446 - 200)),
            ("clear", r"Two hundred and ([\w-]+) days since a page was read out", two(ch - 500 - 200)),
    ):
        m = re.search(pat, date)
        if not m:
            hits.append("no %s clause" % label)
        elif m.group(1) != tail:
            hits.append("%s: %r != %r" % (label, m.group(1), tail))

    fw, fd = divmod(ch - 283, 7)
    exp = ("fever %s weeks and %s day" % (two(fw), two(fd))) if fd else \
          ("fever %s weeks old" % two(fw))
    if exp not in date and exp + "s" not in date:
        hits.append("fever: expected %r" % exp)
    return week, day, hits


if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    vol = sys.argv[3] if len(sys.argv) > 3 else "volume-15"
    total = 0
    for ch in range(lo, hi + 1):
        w, d, hits = check(ch, vol)
        print("ch %d  week %d day %d  %-9s  %s" % (ch, w, d, DAYS[d - 1],
              "OK" if not hits else "; ".join(hits)))
        total += len(hits)
    print("date-line check %d-%d %s: %d hits" % (lo, hi, vol, total))
