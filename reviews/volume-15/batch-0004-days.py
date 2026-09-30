#!/usr/bin/env python3
"""The named-day and relative-pointer sweep for Volume 15 Band 0004.

A NAMED-DAY BACK-REFERENCE IS RESOLVED THROUGH THE FORMULA AND NOT READ, BECAUSE
A REAL DAY OF THE RIGHT NAME IN THE WRONG CHAPTER IS THE DEFECT CLASS THAT NO GATE
SEES AND THAT A READER ALSO MISSES.

  shelf = ch - 125 ; week = 40 + shelf // 7 ; day = shelf % 7 + 1 , day 1 = Tuesday
  the week of a chapter is therefore 40 + (ch-125)//7 and its day-name is the
  mapping  1 Tuesday 2 Wednesday 3 Thursday 4 Friday 5 Saturday 6 Sunday 7 Monday

  OFFSETS APPLIED TO THE WEEK, NOT TO THE DAY:
      last week -1   this week 0   next week +1   a week before -1   a fortnight -2

  A HIT IS (a) a day-name that does not match the chapter it resolves to, or
  (b) a forward-looking phrase that resolves backwards, i.e. next week / a week
  before / a fortnight resolving to a chapter at or before the one it is spoken in.

  `a fortnight` IS WEEK-BASED AND NOT FOURTEEN DAYS, AND `a week before` IS NOT
  THE SAME PHRASE AS `last week` IN EVERY BAND, SO BOTH ARE SWEPT.

RUN ON 701-720 FIRST AS A CALIBRATION, AND PRINT EVERY HIT.
"""
import re
import sys

DAYS = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
DOW = {n: i + 1 for i, n in enumerate(DAYS)}          # day 1 = Tuesday
OFFSETS = {'last week': -1, 'this week': 0, 'next week': +1,
           'a week before': -1, 'a week ago': -1, 'of a week ago': -1,
           'a fortnight': -2, 'of a fortnight': -2, 'a fortnight ago': -2,
           'the week before': -1, 'this morning': None}
PHRASE = re.compile(
    r'\b(?:(?:the|a|an)\s+)?(' + '|'.join(DAYS) + r')\s+of\s+('
    r'last week|this week|next week|a week before|a week ago|of a week ago|'
    r'a fortnight|of a fortnight|a fortnight ago|the week before|this week)\b',
    re.I)
FORWARD = {'next week'}


def week_day(ch):
    shelf = ch - 125
    return 40 + shelf // 7, shelf % 7 + 1


def sweep(lo, hi, vol='volume-15', label=''):
    hits = 0
    for c in range(lo, hi + 1):
        p = f'chapters/{vol}/chapter-{c:04d}.md'
        raw = open(p, encoding='utf-8').read()
        w, d = week_day(c)
        for m in PHRASE.finditer(raw):
            day = m.group(1).capitalize()
            rel = m.group(2).lower()
            off = OFFSETS[rel]
            if off is None:
                continue
            named = DOW[day]
            # the chapter that has that day-name in that week, resolved THROUGH THE
            # FORMULA and not by counting on a finger
            tw = w + off
            # chapter = 125 + (week-40)*7 + (day-1)
            target = 125 + (tw - 40) * 7 + (named - 1)
            okday = True
            if not (651 <= target <= 760):
                okday = False
            okdir = True
            if rel in FORWARD and target <= c:
                okdir = False
            if rel in ('last week', 'a week before', 'a week ago', 'of a week ago',
                       'a fortnight', 'of a fortnight', 'a fortnight ago',
                       'the week before') and target >= c:
                okdir = False
            if not okday or not okdir:
                hits += 1
                line = raw[:m.start()].count('\n') + 1
                bad = []
                if not okday:
                    bad.append(f'resolves to {target}, off the page')
                if not okdir:
                    bad.append(f'{rel} resolves to {target} and does not point '
                               f'the way it says ({c})')
                print(f'  ch{c:04d}:{line}  {m.group(0)!r}  ->  ' + '; '.join(bad))
    print(f'  NAMED-DAY {label or f"{lo}-{hi}"}: {hits} hits.')
    return hits


def relative_pointers(lo, hi, vol='volume-15'):
    """The same class, second half: yesterday, tomorrow, N days ago, of a week
    ago, ten weeks ago. These are a third of the last band's defects."""
    hits = 0
    for c in range(lo, hi + 1):
        p = f'chapters/{vol}/chapter-{c:04d}.md'
        raw = open(p, encoding='utf-8').read()
        for m in re.finditer(r'\b(yesterday|tomorrow|tonight|'
                             r'(\w+|\d+) (?:days?|weeks?|fortnights?) ago)\b', raw, re.I):
            hits += 1
            line = raw[:m.start()].count('\n') + 1
            print(f'  ch{c:04d}:{line}  RELATIVE  {m.group(0)!r}')
    print(f'  RELATIVE POINTERS {lo}-{hi}: {hits} instances, every one READ.')
    return hits


if __name__ == '__main__':
    print('CALIBRATION 701-720 (must be clean on the two categories that can be '
          'checked without knowing what a chapter means):')
    sweep(701, 720, label='701-720')
    print('THE PREVIOUS BAND 721-730:')
    sweep(721, 730, label='721-730')
    print('THE BAND 731-740:')
    sweep(731, 740, label='731-740')
    print()
    print('RELATIVE POINTERS, the band, every instance printed for reading:')
    relative_pointers(731, 740)
