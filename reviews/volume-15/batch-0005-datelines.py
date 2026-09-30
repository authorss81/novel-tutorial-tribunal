#!/usr/bin/env python3
"""Date-line verifier, Volume 15 Band 0005.

THIS IS `batch-0004-datelines.py` WITH ITS OWN TWO LIMITS FIXED, AND THE FIXES
ARE PRINTED, BECAUSE A METHOD THAT STOPS WORKING AT A FIGURE THE LAST CHAPTER
REACHES IS NOT A METHOD AND IS NOT A DEFECT IN THE PROSE.

  1. THE `hall` AND `clear` CLAUSES WERE MATCHED WITH THE LITERAL PREFIX *Two
     hundred and *.  VOLUME 15 REACHED THREE HUNDRED DAYS SINCE THE DIVISION AT
     `746` AND FIVE HUNDRED DAYS SINCE A PAGE WAS READ AT `754`, SO FROM `746`
     ONWARD THE CHECKER REPORTED *no hall clause* ON A CHAPTER THAT WAS RIGHT,
     AND AT `750` IT REPORTED THE SAME ON A CLAUSE THAT WAS ALSO RIGHT.
  2. `ordinal_last('zero')` RAISES ValueError, BECAUSE `500` IS
     *five hundred and zero* TO `two()` AND A MAN WRITES A ROUND HUNDRED AS
     *FIVE HUNDREDTH* AND NOT AS *FIVE HUNDRED AND ZEROTH*.  `750` IS A
     FIVE HUNDREDTH MORNING AND THE CHECKER CRASHED ON IT AND ON NOTHING ELSE.

THE CALIBRATION IS 701-720 AND IT MUST COME BACK CLEAN, AND THE 721-730 AND
731-740 BANDS ARE RUN BECAUSE THE LAST BAND CERTIFIED THEM AND A FIX THAT
BREAKS A CALIBRATION IS NOT A FIX.

  shelf = ch - 125 ; week = 40 + shelf // 7 ; day = shelf % 7 + 1 ; day 1 = Tuesday
  morning = ch - 250 ; settlement = ch - 400 ; fever = ch - 283 days
  hall = ch - 446 ; clear = ch - 500
"""
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
# ⚠ FIX 4, AND IT IS THE ONE THAT TOOK THE LONGEST AND IT IS THE FIFTH
# FAILURE MODE OF THIS PARSER FAMILY THAT THE BAND PROMPT ASKS ABOUT.
# THE TAIL OF AN ORDINAL HAS TO BE PAIRED TO A DIGIT BY THE DIGIT'S OWN VALUE
# AND NOT BY ITS POSITION IN A LIST, BECAUSE THE LIST BEGINS AT *"zero"* AND
# A POSITION IS ONE MORE THAN A VALUE.  THE 0004 SCRIPT PAIRED `ONES[i]` WITH
# `ORDINAL[i + 1]` AND GOT IT RIGHT BY ACCIDENT, BECAUSE IT ONLY EVER CALLED
# THE FUNCTION ON A TENS-ONLY WORD.  REWRITING IT AS `{ONES[i]: ORDINAL[i] for
# i in range(9)}` GIVES `zero: first, one: second, ..., eight: ninth`, WHICH IS
# OFF BY ONE ON EVERY ENTRY, RETURNS NOTHING AT ALL FOR *"nine"*, AND THEN
# RAISES ON THE FIRST FIGURE THAT NEEDS ONE -- WHICH IS *THE HUNDRED AND
# TWENTY-EIGHTH WEEK*, AT `741`, THE FIRST CHAPTER OF THIS BAND.  ALL THREE
# CALIBRATIONS FAILED AT THE SAME PLACE, WHICH IS WHAT A SHARED PARSER FAMILY
# DOES.  THE PAIRING IS NOW BY VALUE, AND THE ASSERTION IS THE GATE, BECAUSE A
# FIGURE NOBODY CHECKS IS A FIGURE NOBODY CAN CATCH.
ONES_ORD = {"one": "first", "two": "second", "three": "third",
            "four": "fourth", "five": "fifth", "six": "sixth",
            "seven": "seventh", "eight": "eighth", "nine": "ninth"}
assert ONES_ORD["one"] == "first" and ONES_ORD["nine"] == "ninth" \
    and "zero" not in ONES_ORD and len(ONES_ORD) == 9
TENS_ORD = {"twenty": "twentieth", "thirty": "thirtieth", "forty": "fortieth",
            "fifty": "fiftieth", "sixty": "sixtieth", "seventy": "seventieth",
            "eighty": "eightieth", "ninety": "ninetieth"}


def two(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
    return str(n)


def words(n):
    """THE WHOLE FIGURE IN WORDS, WHICH THE 0004 SCRIPT COULD NOT DO ABOVE 99.
    A ROUND HUNDRED IS *THREE HUNDRED* AND A ROUND HUNDRED AND FIFTY IS
    *THREE HUNDRED AND FIFTY*, AND NOBODY IN THIS MANUSCRIPT EVER WRITES A
    *ZERO*."""
    if n < 100:
        return two(n)
    h, r = divmod(n, 100)
    return ONES[h] + " hundred" + (" and " + two(r) if r else "")


def ordinal_last(t):
    """'eighty-one' -> 'eighty-first', 'eighty' -> 'eightieth', 'twenty' -> 'twentieth'"""
    # FIX 3, AND IT IS THE SAME ORDERING BUG THE 0004 SCRIPT HAD AND DID NOT
    # CRASH ON: THE HYPHENATED BRANCH MUST BE TAKEN *BEFORE* THE WHOLE-STRING
    # LOOKUP, BECAUSE *twenty-nine* IS A WHOLE STRING THAT IS IN NEITHER
    # DICTIONARY AND THE 0004 SCRIPT ONLY REACHED IT BY NEVER BEING CALLED ON
    # A FIGURE THAT NEEDS IT.
    if "-" in t:
        # ⚠ FIX 5.  THE MANUSCRIPT DOES NOT HYPHENATE AN ORDINAL TAIL: IT WRITES
        # *four hundred and ninety-first*, NOT *four hundred and ninetieth-first*.
        # THE 0004 SCRIPT PRODUCED *ninetieth-first* AND GOT IT RIGHT ONLY BECAUSE
        # IT WAS NEVER CALLED ON A FIGURE WITH A HYPHENATED TAIL IN THE RANGE IT
        # CHECKED, WHICH IS A LUCK AND NOT A METHOD.  THE STEM IS KEPT AS IT IS
        # SPELLED AND ONLY THE TAIL IS TURNED INTO AN ORDINAL.
        head, tail = t.split("-", 1)
        if head in TENS and tail in ONES_ORD:
            return head + "-" + ONES_ORD[tail]
    if t in TENS_ORD:
        return TENS_ORD[t]
    if t in ONES_ORD:
        return ONES_ORD[t]
    raise ValueError(t)


def weekword(w):
    h, r = divmod(w, 100)
    return "hundred" + (" and " + ordinal_last(two(r)) if r else "")


def morningword(n):
    """'four hundred and ninety-first' / 'five hundredth' -- FIX 2."""
    h, r = divmod(n, 100)
    if r == 0:
        return ONES[h] + " hundredth"
    return ONES[h] + " hundred and " + ordinal_last(two(r))


def check(ch, vol="volume-15"):
    path = "chapters/%s/chapter-%04d.md" % (vol, ch)
    lines = open(path, encoding="utf-8").read().splitlines()
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

    m = re.search(r"His (.+?) morning\.", date)
    exp = morningword(ch - 250)
    if not m:
        hits.append("no morning clause")
    elif m.group(1) != exp:
        hits.append("morning: %r != %r" % (m.group(1), exp))

    # FIX 1: THE PREFIX IS NOT *Two hundred and*, IT IS HOWEVER MANY HUNDRED
    # THE FIGURE IS IN.  AT `746` THE HOUSE FORM IS *Three hundred days* AND AT
    # `750` IT IS *Two hundred and fifty days*, AND THE 0004 REGEX COULD SEE
    # NEITHER.
    for label, pat, tail in (
            ("settlement", r"(?:One|Two|Three|Four) hundred(?: and [\w-]+)? days after the settlement\.",
             words(ch - 400)),
            ("hall", r"(?:One|Two|Three|Four) hundred(?: and [\w-]+)? days since the division\.",
             words(ch - 446)),
            ("clear", r"(?:One|Two|Three|Four) hundred(?: and [\w-]+)? days since a page was read out",
             words(ch - 500)),
    ):
        m = re.search(pat, date)
        if not m:
            hits.append("no %s clause" % label)
        elif m.group(0).rsplit(" days", 1)[0].lower() != tail:
            hits.append("%s: %r != %r" % (label, m.group(0).rsplit(" days", 1)[0], tail))

    fw, fd = divmod(ch - 283, 7)
    exp = ("fever %s weeks and %s day" % (two(fw), two(fd))) if fd else \
          ("fever %s weeks old" % two(fw))
    if exp not in date and exp + "s" not in date:
        hits.append("fever: expected %r" % exp)
    return week, day, hits


if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    vol = sys.argv[3] if len(sys.argv) > 3 else "volume-15"
    total = 0
    for ch in range(lo, hi + 1):
        w, d, hits = check(ch, vol)
        print("ch %d  week %d day %d  %-9s  %s" % (ch, w, d, DAYS[d - 1],
              "OK" if not hits else "; ".join(hits)))
        total += len(hits)
    print("date-line check %d-%d %s: %d hits" % (lo, hi, vol, total))