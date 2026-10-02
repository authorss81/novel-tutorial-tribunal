#!/usr/bin/env python3
"""Hand audit of every anchored week-ordinal named-day phrase in a range of chapters.

IT EXISTS BECAUSE `batch-0001-dayrefs.py` CANNOT SEE A WEEK-ORDINAL PHRASE AT ALL:
ITS REGEX IS `(the|a|an)` IN LOWER CASE AND A PHRASE THAT BEGINS A LINE WITH A
CAPITAL IS INVISIBLE TO IT.  THIS SCRIPT RUNS THE CALENDAR OVER EVERY CHAPTER AND
PRINTS, FOR EVERY PHRASE, THE CHAPTER THE PHRASE ACTUALLY NAMES.

  shelf = ch - 125 ; week = 40 + shelf // 7 ; day = shelf % 7 + 1 ; day 1 = Tuesday

IT PRINTS A COUNT.  A COUNT IS NOT A FINDING.  THE FINDING IS WHAT A PERSON DOES
WITH THE COUNT.
"""
import re
import os
import sys

DAYS = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
ORD = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5,
       'sixth': 6, 'seventh': 7}
TENS = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
TENSO = {10: 'tenth', 20: 'twentieth', 30: 'thirtieth', 40: 'fortieth',
         50: 'fiftieth', 60: 'sixtieth', 70: 'seventieth', 80: 'eightieth',
         90: 'ninetieth'}
ONES = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine'}
ORDONES = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth',
           6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth'}


def ordinal(n):
    """THE COMPOUND IS THE CARDINAL TENS WORD PLUS THE ORDINAL UNIT:
    FORTY + NINTH IS *FORTY-NINTH* AND NOT *FORTIETH-NINTH*, AND A BARE TENS WORD
    IS THE ORDINAL ITSELF, *FIFTIETH*.  GETTING THAT WRONG IS HOW A SCRIPT ENDS
    UP CALLING EVERY PHRASE UNANCHORED AND HOW A PERSON THEN BELIEVES IT."""
    if n >= 100:
        b = n - 100
        return 'hundredth' + (' ' + ordinal(b) if b else '')
    t, u = n // 10 * 10, n % 10
    if t == 0:
        return ORDONES[u]
    if u == 0:
        return TENSO[t]
    return TENS[t] + '-' + ORDONES[u]


def week_word(n):
    """THE MANUSCRIPT FORM: *the hundred and forty-ninth week*."""
    if n >= 100:
        b = n - 100
        return 'hundredth' if b == 0 else 'hundred and ' + ordinal(b)
    return ordinal(n)


def cal(ch):
    s = ch - 125
    return 40 + s // 7, s % 7 + 1


def main(lo, hi, vol):
    inv = {'the ' + week_word(n) + ' week': n for n in range(41, 200)}
    bywd = {}
    for cand in range(1, 1200):
        bywd.setdefault(cal(cand), cand)
    pat = re.compile(r'\bthe (first|second|third|fourth|fifth|sixth|seventh)'
                     r'(?: and last)? day of (the [a-z\- ]+? week)\b', re.I)
    patw = re.compile(r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)s?'
                      r' of (the [a-z\- ]+? week)\b', re.I)
    total = ok = 0
    bad = []
    refs = []
    per = {}
    d = os.path.join('chapters', vol)
    for f in sorted(os.listdir(d)):
        m = re.match(r'chapter-(\d+)\.md$', f)
        if not m:
            continue
        ch = int(m.group(1))
        if not (lo <= ch <= hi):
            continue
        c = 0
        for i, line in enumerate(open(os.path.join(d, f), encoding='utf-8').read().split('\n'), 1):
            for mm in pat.finditer(line):
                total += 1
                c += 1
                wname = mm.group(2).lower()
                dnum = ORD[mm.group(1).lower()]
                if wname not in inv:
                    bad.append((f, i, mm.group(0), 'NO WEEK WORD'))
                    continue
                w = inv[wname]
                t = bywd.get((w, dnum))
                if t == ch:
                    ok += 1
                else:
                    refs.append((f, i, t, mm.group(0)))
            for mm in patw.finditer(line):
                total += 1
                c += 1
                wname = mm.group(2).lower()
                dnum = DAYS.index(mm.group(1).capitalize()) + 1
                if wname not in inv:
                    bad.append((f, i, mm.group(0), 'NO WEEK WORD'))
                    continue
                w = inv[wname]
                t = bywd.get((w, dnum))
                if t == ch:
                    ok += 1
                else:
                    refs.append((f, i, t, mm.group(0)))
        per[ch] = c
    print('ANCHORED NAMED-DAY PHRASES, COUNTED BY HAND: %d' % total)
    print('  ON THE CHAPTER IT IS IN: %d' % ok)
    print('  BACKWARD REFERENCES, EACH WITH THE CHAPTER IT NAMES: %d' % len(refs))
    print('  UNANCHORED OR IMPOSSIBLE: %d' % len(bad))
    print()
    print('THE REFERENCES, ONE A LINE, FOR A PERSON TO CHECK AGAINST THE CHAPTER IT NAMES:')
    for r in refs:
        print('  %s:%d  names %s  %s' % r)
    print()
    for b in bad:
        print('  IMPOSSIBLE', b)
    print('per chapter:', per)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))
