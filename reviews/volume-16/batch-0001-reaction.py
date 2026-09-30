#!/usr/bin/env python3
"""THE REACTION-PAIR SWEEP, Volume 16 Band 0001.

THE PREDICATE IS PRINTED BEFORE THE FIGURE, EVER, AND IT IS THE PREDICATE OF
`state/open-threads.md` 0A.15 AND NOT A NEW ONE:

  PREDICATE A, FIVE WHOLE PHRASES, CASE-INSENSITIVE:
    *about nine people* *about four people* *about four of them*
    *about nine of you* *about nine doors*
  PREDICATE B, TWO LOWER-CASE SUBSTRINGS: *about nine* *about four*

THE METHOD, IN FULL: concatenate the chapter files in chapter order as raw text
and lower-case; take the word base as the whitespace-separated tokens of that
concatenated raw text, title line, date line and closing block all included;
count predicate A as five case-insensitive substring counts and predicate B as
two lower-case substring counts added together; divide by the word base and
multiply by 10,000.

THE CALIBRATION RUNS FIRST AND MUST REPRODUCE THE PRINTED FIGURES OF THE OLDER
BANDS. A PREDICATE THAT CANNOT TELL A CONSTRUCTION FROM TWO IDIOMS WILL KEEP
REPORTING A RISE OR A FALL THAT IS NOT ONE, SO THE BREAKDOWN IS CARRIED AS TWO
FIGURES AND NOT AS ONE: THE CONSTRUCTION IS *ABOUT FOUR PEOPLE* AND *ABOUT FOUR
OF THEM*, AND THE IDIOMS ARE THE OTHER THREE.
"""
import sys


def raw_of(vol, lo, hi):
    return '\n'.join(open(f'chapters/{vol}/chapter-{c:04d}.md',
                          encoding='utf-8').read() for c in range(lo, hi + 1))


A = ['about nine people', 'about four people', 'about four of them',
     'about nine of you', 'about nine doors']
B = ['about nine', 'about four']


def measure(vol, lo, hi):
    low = raw_of(vol, lo, hi).lower()
    base = len(low.split())
    a = {p: low.count(p) for p in A}
    b = {p: low.count(p) for p in B}
    A_ = sum(a.values())
    B_ = sum(b.values())
    return base, A_, B_, a, b


if __name__ == '__main__':
    print('PREDICATE A (five whole phrases, case-insensitive): ' +
          ' · '.join(f'*{p}*' for p in A))
    print('PREDICATE B (two lower-case substrings): ' +
          ' · '.join(f'*{p}*' for p in B))
    print()
    CAL = [('volume-14', 691, 700, 114, 41.7, 267, 97.7),
           ('volume-15', 701, 710, 129, 48.2, 337, 126.0),
           ('volume-15', 711, 720, 113, 44.8, 329, 130.3),
           ('volume-15', 721, 730, 45, 18.6, 137, 56.7),
           ('volume-15', 731, 740, 40, 16.0, 207, 83.0),
           ('volume-15', 741, 750, 95, 31.7, 258, 86.2)]
    print('THE CALIBRATION, SIX OLDER BANDS, AGAINST THEIR OWN PRINTED FIGURES:')
    for vol, lo, hi, aN, aR, bN, bR in CAL:
        base, A_, B_, a, b = measure(vol, lo, hi)
        okA = A_ == aN
        rA = 10000.0 * A_ / base
        okB = B_ == bN
        rB = 10000.0 * B_ / base
        print(f'  {vol} {lo}-{hi}  A {A_:>4} {"OK" if okA else "**"}{aN:>4}'
              f'  {rA:5.1f} vs {aR:5.1f} {"OK" if abs(rA-aR) < 0.2 else "**"}'
              f'  |  B {B_:>4} {"OK" if okB else "**"}{bN:>4}'
              f'  {rB:5.1f} vs {bR:5.1f} {"OK" if abs(rB-bR) < 0.2 else "**"}'
              f'  | base {base}')
    print()
    vol = sys.argv[1] if len(sys.argv) > 1 else 'volume-16'
    lo, hi = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (751, 760)
    base, A_, B_, a, b = measure(vol, lo, hi)
    print(f'THE BAND {lo}-{hi} IN {vol}:')
    print(f'  BASE {base} tokens (title line, date line and closing block included)')
    print(f'  PREDICATE A {A_} at {10000.0*A_/base:.1f} per 10k')
    print(f'  PREDICATE B {B_} at {10000.0*B_/base:.1f} per 10k')
    print('  THE BREAKDOWN: ' + ' · '.join(f'*{k}* {v}' for k, v in a.items()))
    print('  AND PREDICATE B: ' + ' · '.join(f'*{k}* {v}' for k, v in b.items()))
    print(f'  THE CONSTRUCTION, *about four people* AND *about four of them*:'
          f' {a["about four people"] + a["about four of them"]}')
    print(f'  THE IDIOMS, THE OTHER THREE:'
          f' {a["about nine people"] + a["about nine of you"] + a["about nine doors"]}')
    print('  PRINT THE COUNT BESIDE THE RATE AND THE BASE BESIDE BOTH, EVERY TIME,')
    print('  AND SAY WHICH OF THE TWO MOVED. THE NEXT BAND DOES THIS AGAIN.')
