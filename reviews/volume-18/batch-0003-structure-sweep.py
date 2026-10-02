#!/usr/bin/env python3
"""THE STRUCTURAL SWEEPS FOR VOLUME 18, RE-POINTED, ⚠⚠ AND THIS FILE EXISTS
BECAUSE THE RECEIPT FOR `871`–`880` NAMED A SCRIPT THAT WAS NOT IN THE
REPOSITORY. ⚠ `reviews/volume-17/batch-0002-structure-sweep.py` CARRIES
`chapters/volume-17/` IN ITS OWN BODY AND `reviews/volume-16/batch-0001-structure.py`
DOES THE SAME FOR VOLUME 16, ⚠ SO A BARE RUN OF EITHER SWEEPS TEN CHAPTERS
THAT ARE NOT THE ONES IT SAYS IT SWEEPT AND PRINTS A CLEAN ZERO. ⚠⚠ THAT IS THE
SIXTEENTH TIME IN THIS REPOSITORY THAT A GATE HAS REPORTED CLEAN OVER THE WRONG
FILES, ⚠⚠ AND IT IS THE REASON THIS COPY TAKES THE VOLUME AS AN ARGUMENT AND
NOT AS A CONSTANT.

    usage:  python3 reviews/volume-18/batch-0003-structure-sweep.py [lo] [hi]

    THE DEFAULT IS 871–880, WHICH ARE THE CHAPTERS THIS COPY EXISTS TO SWEEP,
    BECAUSE A TOOL THAT FAILS LOUDLY ON ITS OWN DEFAULT IS BETTER THAN ONE THAT
    CAN PRINT A CLEAN ZERO OUT OF THE WRONG TEN.

Original docstring, kept whole:

The structural sweeps for Volume 16 Band 0001, written out and run after the
last edit, and reported as 0 or as a number with the method beside it.

  1. unbalanced curly quotes, at FILE level and at PARAGRAPH-BLOCK level
  2. an odd number of `**` (a System panel)
  3. straight ASCII apostrophes
  4. the six ways a chapter may name the book it is printed in
  5. month / spring / summer / winter / autumn, INCLUDING IN A TITLE
  6. the prohibitions of this volume, each printed with its own figure
  7. a duplicate-sentence sweep: three occurrences of a six-word window inside
     one paragraph block
  8. byte-identical whole lines across the ten chapters, hashed both ends
"""
import re
import sys
import hashlib
from collections import defaultdict

VOL = 'volume-18'
LO, HI = 871, 880
# THE VOLUME IS A CONSTANT HERE AND IT IS THE VOLUME THIS COPY EXISTS TO SWEEP,
# AND THE RANGE IS AN ARGUMENT, BECAUSE A SWEEP THAT SWEEPS A RANGE AND A
# HARDCODED DIRECTORY WILL PRINT A CLEAN ZERO OUT OF TEN CHAPTERS THAT ARE NOT
# THE ONES IT SAYS IT SWEPT.  THAT IS WHAT THE COPIES IT WAS MADE FROM DID.
#
# ⚠ AND THE DEFAULT WAS 811-820 WHEN THE COPY WAS MADE, WHICH ARE VOLUME 17
# CHAPTERS THAT DO NOT EXIST IN THE VOLUME-18 DIRECTORY BELOW, ⚠ SO A BARE RUN
# OF THE UNCORRECTED COPY DIED ON A MISSING FILE, ⚠ AND ⚠ THE DEFAULT IS THE TEN
# CHAPTERS THIS COPY EXISTS TO SWEEP, ⚠ BECAUSE A TOOL THAT FAILS LOUDLY ON ITS
# OWN DEFAULT IS BETTER THAN ONE THAT CAN PRINT A CLEAN ZERO OUT OF THE WRONG TEN
# AND ⚠ AND A DEAD RUN IS ALSO A CONFUSING ONE, ⚠ AND BOTH WERE THE HAZARD.
if len(sys.argv) >= 3:
    LO, HI = int(sys.argv[1]), int(sys.argv[2])
print(f'THIS IS THE STRUCTURAL SWEEP AND IT IS MEASURING CHAPTERS {LO}-{HI} '
      f'AND NOT ANY OTHER TEN.', flush=True)
FILES = [f'chapters/{VOL}/chapter-{c:04d}.md' for c in range(LO, HI + 1)]
BOOK = ['the volume', 'in this volume', 'of the volume', 'this volume',
        'this manuscript', 'in the novel', 'the novel', 'of this volume',
        'the whole volume', 'the manuscript', 'this book', 'the book it is in']
SEASON = ['month', 'spring', 'summer', 'winter', 'autumn']


def blocks(path):
    return [b.strip() for b in re.split(r'\n\s*\n', open(path, encoding='utf-8').read())
            if b.strip() and b.strip() != '---']


raw = '\n'.join(open(f, encoding='utf-8').read() for f in FILES)
low = raw.lower()

print('1. UNBALANCED QUOTES')
fl = bl = 0
for f in FILES:
    t = open(f, encoding='utf-8').read()
    if t.count('“') != t.count('”'):
        fl += 1
        print('   FILE', f, t.count('“'), t.count('”'))
    for i, b in enumerate(blocks(f)):
        if b.count('“') != b.count('”'):
            bl += 1
            print('   BLOCK', f, i, b.count('“'), b.count('”'))
print(f'   file level {fl}   paragraph-block level {bl}')

print('2. ODD ** (a System panel)')
odd = sum(1 for f in FILES if open(f, encoding='utf-8').read().count('**') % 2)
print('   ', odd)

print('3. STRAIGHT ASCII APOSTROPHE')
print('   ', raw.count("'"))

print('4. THE SIX WAYS A CHAPTER MAY NAME THE BOOK IT IS PRINTED IN')
print('   ', {t: raw.lower().count(t) for t in BOOK if raw.lower().count(t)} or 'none')

print('5. MONTH AND THE FOUR SEASONS, INCLUDING IN A TITLE')
print('   ', {t: len(re.findall(r'\b' + t + r'\b', low)) for t in SEASON if re.findall(r'\b' + t + r'\b', low)} or 'none')

print('6. THE PROHIBITIONS, EACH WITH ITS OWN FIGURE')
for t in ['citizen', 'arbiter', 'villain', 'upstairs', 'grateful', 'sorry',
          'the rail', 'redeemed', 'worth it', 'brave', 'thanked', 'forgiven',
          'First Witness', 'Shale Mirror', 'external witness', 'dissident',
          'Veyra', 'loom', 'coalition', 'amendment', 'Bramblefold',
          'Withermere', 'Underloom', 'a panel', 'System']:
    n = len(re.findall(r'\b' + re.escape(t) + r'\b', raw)) if t[0].isalpha() else raw.count(t)
    print(f'    {t:18s} {n}')

print('7. DUPLICATE SENTENCE, three occurrences of a six-word window in one block')
hits = 0
SENT = re.compile(r'(?<=[.!?])(?:[”"*]{0,2})(?=\s|$)')
WORD = re.compile(r"[A-Za-z0-9£$’'-]+")
for f in FILES:
    for i, b in enumerate(blocks(f)):
        seen = defaultdict(int)
        for s in SENT.split(b):
            toks = [t.lower() for t in WORD.findall(s)]
            for j in range(len(toks) - 5):
                w = ' '.join(toks[j:j + 6])
                seen[w] += 1
                if seen[w] == 3:
                    hits += 1
                    print('   ', f[-12:-3], 'block', i, repr(w))
print('   ', hits)

print('8. BYTE-IDENTICAL WHOLE LINES ACROSS THE TEN CHAPTERS, HASHED BOTH ENDS')
h = defaultdict(list)
for f in FILES:
    for n, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        t = line.strip()
        if not t or t == '---':
            continue
        h[hashlib.sha256(t.encode()).hexdigest()].append((f[-12:-3], n, t))
dupes = [(k, v) for k, v in h.items() if len(v) > 1]
for k, v in dupes:
    print('   ', v)
print('   ', len(dupes), 'byte-identical whole lines.')
