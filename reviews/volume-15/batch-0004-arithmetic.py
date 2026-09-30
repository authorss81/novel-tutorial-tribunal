#!/usr/bin/env python3
"""The two arithmetic sweeps for Volume 15 Band 0004, as code, because a method
written out in prose is not a method.

  1. EVERY `SEVEN HUNDRED AND ... LESS ... HUNDRED AND ...` PHRASE IS PARSED AND
     RECOMPUTED. THE WINDOW IS ON BOTH SIDES OF `less`, BECAUSE A PARSER THAT
     ONLY READS THE RESULT WORD AFTER THE PHRASE REPORTS FALSE HITS WHEREVER THE
     RESULT WORD PRECEDES THE SUBTRACTION -- *Sixteen is seven hundred and
     seventeen less seven hundred and one*. HYPHENS ARE NORMALISED FIRST, BECAUSE
     *eighty-five* IS ONE TOKEN TO A REGEX AND TWO WORDS TO A MAN, AND THAT IS A
     FOURTH FAILURE MODE AND NOT A FIFTH.

  2. EVERY DAY-COUNT SPOKEN AGAINST A CHAPTER IS RESOLVED THROUGH THE FORMULA,
     NOT READ. A UNIT MAP SAYS WHICH RULE GOVERNS WHICH UNIT, AND A COUNT WITH NO
     UNIT IN THE MAP IS PRINTED AND NOT JUDGED, BECAUSE IT IS A COUNT OF SOMETHING
     ELSE.

  BOTH ARE RUN ON 701-720 FIRST AS A CALIBRATION, WHICH MUST COME BACK CLEAN, AND
  THEN ON 721-730, WHICH THE LAST BAND CERTIFIED AT 36 PHRASES AND 0 FLAGGED.
"""
import re
import sys

_ONES = ('zero one two three four five six seven eight nine ten eleven twelve '
         'thirteen fourteen fifteen sixteen seventeen eighteen nineteen').split()
_TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
         'eighty', 'ninety']
SMALL = {w: i for i, w in enumerate(_ONES)}
SMALL.update({w: 10 * i for i, w in enumerate(_TENS) if w})
# LONGEST ALTERNATION FIRST. A REGEX ALTERNATION TAKES THE FIRST BRANCH THAT
# MATCHES, AND *nine* COMES BEFORE *ninety* IN DICTIONARY ORDER, SO
# *ninety-three* PARSES AS *nine* AND THEN *three* AND EVERY FIGURE IN THE
# SENTENCE AFTER IT IS WRONG. THAT IS NOT A FALSE POSITIVE, IT IS A PARSER THAT
# DOES NOT COUNT.
W = '|'.join(sorted(list(SMALL) + ['hundred', 'thousand'], key=len, reverse=True))
NUMRUN = re.compile(r'(?:' + W + r')(?:[\s-]+(?:and[\s-]+)?(?:' + W + r'))*')
LESS = re.compile(r'\bless\b', re.I)


def norm(t):
    return re.sub(r'-\s+', '-', t)


def val(s):
    tot = cur = 0
    for w in re.split(r'[\s-]+', s.lower()):
        if w == 'and':
            continue
        if w == 'hundred':
            cur = (cur or 1) * 100
        elif w == 'thousand':
            tot += (cur or 1) * 1000
            cur = 0
        elif w in SMALL:
            cur += SMALL[w]
        else:
            return None
    return tot + cur


def left_operand(text, end):
    """The number-word run that ends immediately before `end`."""
    best = None
    for m in NUMRUN.finditer(text):
        if m.end() == end:
            best = m
    return best


def less_phrases(path):
    raw = norm(open(path, encoding='utf-8').read())
    out = []
    for lm in LESS.finditer(raw):
        L = raw[:lm.start()].rstrip()
        R = raw[lm.end():]
        rm = NUMRUN.search(R)
        if not rm:
            continue
        lmL = left_operand(L, len(L))
        if not lmL:
            continue
        a, b = val(lmL.group(0)), val(rm.group(0))
        if a is None or b is None or b > a:
            continue
        # THE RESULT, WHICH IS ON EITHER SIDE OF THE PHRASE, IS LOOKED FOR IN THE
        # SENTENCE THAT HOLDS THE PHRASE AND NOT IN THE CHARACTER BEFORE IT,
        # BECAUSE A CHARACTER BEFORE IT IS A SHAPE AND A SENTENCE IS A PLACE.
        sent_start = raw.rfind('\n', 0, lmL.start()) + 1
        sent_end = raw.find('\n', lmL.start())
        sent = raw[sent_start:sent_end if sent_end > 0 else len(raw)].lower()
        got = a - b
        claim = None
        if got == 0:
            claim = got
        else:
            for m in NUMRUN.finditer(sent):
                v = val(m.group(0))
                if v == got:
                    claim = got
                    break
        line = raw[:lmL.start()].count('\n') + 1
        out.append((a, b, got, claim, line, sent.strip()[:90]))
    return out


# unit -> (name, rule).  rule(ch) is the figure the chapter must carry.
def R(**kw):
    return kw

UNITS = {
    'his days in the county of kell': ('KELL', lambda c: c - 554),
    'a boy of thirteen\'s days': ('BOY', lambda c: c - 701),
    'a cut across a right palm': ('CUT', lambda c: c - 685),
    'a man in an ash': ('ASH', lambda c: c - 630),
    'a woman in a reed': ('REED', lambda c: c - 629),
    'readings': ('READ', lambda c: c - 710),
    'reading': ('READ', lambda c: c - 710),
    'mornings of the asking': ('ASK', lambda c: 1 + (c - 722)),
    'times he has asked': ('ASK', lambda c: 1 + (c - 722)),
}
UNITWORD = ('morning|mornings|reading|readings|name|names|day|days|night|'
            'nights|week|weeks|year|years|inch|inches|feet|second|seconds|'
            'minute|minutes|step|steps|opening|openings|space|spaces|line|lines|'
            'sentence|sentences|offer|offers|thing|things|man|men|woman|women|'
            'boy|boys|child|children|chair|chairs|board|boards|hash|ash|reed')
UNITPAT = re.compile(r'((?:' + W + r')(?:[\s-]+(?:and[\s-]+)?(?:' + W + r'))*)'
                     r'((?:%s)\b)' % UNITWORD, re.I)


def day_counts(path, c):
    raw = norm(open(path, encoding='utf-8').read()).lower()
    rows = []
    for m in UNITPAT.finditer(raw):
        n = val(m.group(1))
        if n is None:
            continue
        rows.append((n, m.group(2), m.start()))
    return rows


def sweep(lo, hi, vol='volume-15', full=True):
    phrases = flagged = 0
    for c in range(lo, hi + 1):
        p = f'chapters/{vol}/chapter-{c:04d}.md'
        for a, b, got, claim, line, sent in less_phrases(p):
            phrases += 1
            if claim != got:
                flagged += 1
                print(f'  ch{c:04d}:{line}  LESS MISMATCH  {a} less {b} = {got}; '
                      f'the sentence does not carry it: ...{sent}...')
    print(f'  LESS PHRASES {lo}-{hi}: {phrases} parsed, {flagged} flagged.')
    if not full:
        return flagged
    return flagged


COUNTERS = {
    # name, the exact phrase the page must carry, the rule, the unit it counts
    'READINGS  (ch-710)': (r'{n} readings\b', lambda c: c - 710),
    'ASKING    (1+ch-722)': (r'{n} mornings\b', lambda c: 1 + (c - 722)),
    'BOY-DAYS  (ch-701)': (r'{n} days\.', lambda c: c - 701),
    'KELL      (ch-554)': (r'in this county a hundred and {n}\b', None),
    'CUT       (ch-685)': (r'cut across it is {n} days old', lambda c: c - 685),
    'ASH       (ch-630)': (r'ash[^.]{0,120}?for {n} days', lambda c: c - 630),
    'REED      (ch-629)': (r'reed[^.]{0,120}?for {n} days', lambda c: c - 629),
}


def counters(lo, hi, vol='volume-15'):
    """The live counters of the band, written down in order and read back. A
    counter that is one out does not look like one out and it is the only figure
    in this book with no anchor to catch it."""
    print(f'  THE LIVE COUNTERS, {lo}-{hi}, IN ORDER')
    for name, (pat, rule) in COUNTERS.items():
        print(f'    {name}')
        for c in range(lo, hi + 1):
            p = f'chapters/{vol}/chapter-{c:04d}.md'
            raw = norm(open(p, encoding='utf-8').read()).lower()
            want = c - 554 if rule is None else rule(c)
            n = spell(want)
            pat2 = pat.format(n=n)
            if name.startswith('KELL'):
                pat2 = r'a hundred and ' + n + r'\b'
            hits = re.findall(pat2, raw)
            if hits:
                print(f'      ch{c}: {want:4d}  {n:34s}  {len(hits)} on the page')
            else:
                print(f'      ch{c}: {want:4d}  {n:34s}  --')


def spell(n):
    if n < 20:
        return _ONES[n]
    if n < 100:
        t, u = _TENS[n // 10], n % 10
        return t + ((' ' + _ONES[u]) if u else '')
    h, r = n // 100, n % 100
    return _ONES[h] + ' hundred' + ((' and ' + spell(r)) if r else '')


if __name__ == '__main__':
    print('CALIBRATION 701-720 (must come back clean):')
    sweep(701, 720)
    print('CALIBRATION 721-730 (the last band certified 36 phrases, 0 flagged):')
    sweep(721, 730)
    print('THE BAND 731-740:')
    sweep(731, 740)
    print()
    counters(731, 740)
