#!/usr/bin/env python3
"""The arithmetic sweeps for Volume 15 Band 0004, as code, because a method
written out in prose is not a method.

1. EVERY `SEVEN HUNDRED AND ... LESS ... HUNDRED AND ...` PHRASE IS PARSED AND
   RECOMPUTED.  THE WINDOW IS ON BOTH SIDES OF `less`, BECAUSE A PARSER THAT
   ONLY READS THE RESULT WORD AFTER THE PHRASE REPORTS FALSE HITS WHEREVER THE
   RESULT WORD PRECEDES THE SUBTRACTION -- *Sixteen is seven hundred and
   seventeen less seven hundred and one*.  HYPHENS ARE NORMALISED BOTH WAYS,
   BECAUSE *eighty-five* IS ONE TOKEN TO A REGEX AND TWO WORDS TO A MAN.

   THE RESULT IS LOOKED FOR IN THE WHOLE PARAGRAPH BLOCK THE PHRASE IS IN AND NOT
   IN THE SINGLE LINE, BECAUSE A MAN PUTS THE FIGURE IN ONE SENTENCE AND THE
   WORKING IN THE NEXT AND A LINE IS NOT A PLACE.  THE CALIBRATION CATCHES THIS:
   AT `712` THE FIGURE IS *a hundred and fifty-eight* ON ONE LINE AND THE
   WORKING IS *seven hundred and twelve less five hundred and fifty-four* ON THE
   NEXT, AND A ONE-LINE WINDOW FLAGS IT AND IS WRONG.

2. THE LIVE COUNTERS ARE WRITTEN DOWN IN ORDER AND READ BACK.  A COUNTER THAT IS
   ONE OUT DOES NOT LOOK LIKE ONE OUT AND IT IS THE ONLY FIGURE IN THIS BOOK WITH
   NO ANCHOR TO CATCH IT.  ⚠ THIS SWEEP CAUGHT A REAL ONE OUT IN THE LAST BAND.

BOTH ARE RUN ON 701-720 FIRST AS A CALIBRATION, WHICH MUST COME BACK CLEAN.
"""
import re
import sys

_ONES = ('zero one two three four five six seven eight nine ten eleven twelve '
         'thirteen fourteen fifteen sixteen seventeen eighteen nineteen').split()
_TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
         'eighty', 'ninety']
SMALL = {w: i for i, w in enumerate(_ONES)}
SMALL.update({w: 10 * i for i, w in enumerate(_TENS) if w})
# LONGEST ALTERNATION FIRST.  A REGEX ALTERNATION TAKES THE FIRST BRANCH THAT
# MATCHES, AND *nine* COMES BEFORE *ninety*, SO *ninety-three* PARSES AS *nine*
# AND THEN *three* AND EVERY FIGURE IN THE SENTENCE AFTER IT IS WRONG.
W = '|'.join(sorted(list(SMALL) + ['hundred', 'thousand'], key=len, reverse=True))
NUMRUN = re.compile(r'(?:' + W + r')(?:[\s-]+(?:and[\s-]+)?(?:' + W + r'))*')
LESS = re.compile(r'\bless\b', re.I)


def norm(t):
    t = t.lower().replace('’', "'")
    # HORIZONTAL WHITESPACE ONLY.  `\s` INCLUDES THE NEWLINE, AND A HYPHEN AT
    # THE END OF A LINE IS AN EM DASH IN THE HOUSE FORM, SO COLLAPSING `-\s+`
    # JOINS TWO LINES AND EVERY LINE NUMBER AFTER IT IS WRONG.  THAT IS A FIFTH
    # FAILURE MODE OF THIS PARSER AND NOT A DEFECT IN THE TEXT.
    t = re.sub(r'-[ \t]+', '-', t)
    t = re.sub(r'[ \t]*-[ \t]*', '-', t)
    t = re.sub(r'[ \t]+', ' ', t)
    return t


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


def spell(n):
    if n < 20:
        return _ONES[n]
    if n < 100:
        t, u = _TENS[n // 10], n % 10
        return t + (('-' + _ONES[u]) if u else '')
    h, r = n // 100, n % 100
    return _ONES[h] + 'hundred' + (('-' + spell(r)) if r else '')


def aspell(n):
    """the form the page uses: *a hundred and seventy-seven*, *a hundred and ten*"""
    if n < 100:
        return spell(n)
    if n < 1000:
        # THE PAGE SPELLS *A HUNDRED AND SEVENTY-SEVEN*, NOT *... SEVENTY AND SEVEN*.
        # AN EARLIER VERSION OF THIS FUNCTION REPLACED THE HYPHEN INSIDE THE TENS
        # AND SAID EVERY FIGURE ABOVE A HUNDRED WAS ONE OUT.  IT WAS THE FUNCTION.
        return 'a hundred' + (' and ' + spell(n - 100) if n % 100 else '')
    return str(n)


def hspell(n):
    """the form a character block uses: *a hundred and seventy-seven* / *hundred and seventy-eight*"""
    return aspell(n)


def isq(t):
    t = t.strip()
    return t.startswith('\u201c*') or t.startswith('\u201c') or t.endswith('\u201d')


def block_of(lines, i):
    """THE UNIT A MAN SPEAKS IN IS THE RUN OF QUOTED LINES, NOT THE PARAGRAPH
    BLOCK, AND THE TWO ARE NOT THE SAME THING IN EVERY CHAPTER: AT `712` EVERY
    QUOTED LINE STANDS ALONE WITH A BLANK LINE BOTH SIDES OF IT, SO A PARAGRAPH
    BLOCK IS ONE LINE AND A FIGURE GIVEN IN ONE SENTENCE WITH ITS WORKING IN THE
    NEXT READS AS TWO UNRELATED LINES.  A PARAGRAPH-BLOCK WINDOW WAS TRIED FIRST
    AND FLAGGED `712`, WHICH IS A FALSE HIT."""
    a = b = i
    def prev(j):
        while j >= 0 and not lines[j].strip():
            j -= 1
        return j
    def nxt(j):
        while j < len(lines) and not lines[j].strip():
            j += 1
        return j
    j = prev(i - 1)
    while j >= 0 and isq(lines[j]):
        a = j
        j = prev(j - 1)
    j = nxt(i + 1)
    while j < len(lines) and isq(lines[j]):
        b = j
        j = nxt(j + 1)
    return norm(' '.join(lines[a:b + 1]))


def less_phrases(path):
    raw = norm(open(path, encoding='utf-8').read())
    lines = open(path, encoding='utf-8').read().splitlines()
    out = []
    for lm in LESS.finditer(raw):
        L = raw[:lm.start()].rstrip()
        rm = NUMRUN.search(raw[lm.end():])
        if not rm:
            continue
        best = None
        for m in NUMRUN.finditer(L):
            if m.end() == len(L):
                best = m
        if not best:
            continue
        a, b = val(best.group(0)), val(rm.group(0))
        if a is None or b is None or b > a:
            continue
        got = a - b
        ln = raw[:best.start()].count('\n') + 1
        blk = block_of(lines, ln - 1)
        claim = any(val(m.group(0)) == got for m in NUMRUN.finditer(blk))
        out.append((a, b, got, claim, ln, blk[:110]))
    return out


def sweep(lo, hi, vol='volume-16'):
    phrases = flagged = 0
    for c in range(lo, hi + 1):
        p = f'chapters/{vol}/chapter-{c:04d}.md'
        for a, b, got, claim, line, blk in less_phrases(p):
            phrases += 1
            if not claim:
                flagged += 1
                print(f'  ch{c:04d}:{line}  LESS MISMATCH  {a} less {b} = {got}; '
                      f'no figure in the block: ...{blk}...')
    print(f'  LESS PHRASES {lo}-{hi} {vol}: {phrases} parsed, {flagged} flagged.')
    return flagged


# THE FIGURE A CHARACTER BLOCK PUTS IN, SPELLED THE WAY THE PAGE SPELLS IT
COUNTERS = [
    ('READINGS   ch-710  (a man of thirty-eight reads the sheet)',
     r'\b([a-z-]+) readings\b', lambda c: c - 710, spell, 'garrin tolley'),
    ('SHEET-READ ch-710  (the same count, said as *read that sheet N times*)',
     # A MAN OF THIRTY-EIGHT GIVES THIS COUNT TWO WAYS ON THE PAGE AND BOTH
     # ARE THE SAME COUNT: *HAS READ THAT SHEET N TIMES* AND *N MORNINGS*.
     # A PATTERN THAT TAKES ONLY ONE OF THEM REPORTS THE OTHER AS ONE OUT.
     # VOLUME 16, AND THE FIX IS THE FINDING THIS SWEEP EXISTS FOR. THE SECOND
     # PATTERN BELOW IS *N IS SEVEN HUNDRED AND <X> LESS SEVEN HUNDRED AND TEN*.
     # THE SENTENCE IT MATCHES IS THE ONE THE MAN OF THIRTY-EIGHT AND THE WOMAN
     # OF THIRTY-FOUR AND THE WOMAN OF TWENTY-EIGHT ALL USE TO GIVE A WORKED
     # SUBTRACTION IN FRONT OF ABOUT NINE PEOPLE, AND IT IS THE ONLY SENTENCE
     # THE MAN OF THIRTY-EIGHT USES FOR HIS COUNT IN 751-760. THE PATTERN AS IT
     # STOOD MATCHED *N MORNINGS*, WHICH HE STOPPED SAYING ABOUT HIMSELF WHEN HE
     # DECIDED TO STOP DECIDING, AND SO ON ARRIVAL IT REPORTED NINE ONE OUTS ON A
     # BAND THAT WAS CLEAN. THE PATTERN IS ANCHORED ON *GARRIN TOLLEY* SO THAT IT
     # CANNOT TAKE A LINE OFF A BOY OF THIRTEEN WHO ALSO GIVES A WORKED
     # SUBTRACTION IN WORDS, WHICH IT DID ON THE FIRST ATTEMPT.
     (r'has read that sheet ([a-z-]+) times',
      r'([a-z-]+) is seven hundred and [a-z-]+ less seven hundred and ten'),
     lambda c: c - 710, spell, 'garrin tolley'),
    ('ASKING     1+ch-722 (a man of fifty-four\'s mornings)',
     r'\b([a-z-]+) mornings\b', lambda c: 1 + (c - 722), spell, 'barnaby crove'),
    ('KELL       ch-554  (his days in the county of Kell)',
     r'in this county (a hundred and [a-z -]+?) days', lambda c: c - 554, aspell, 'ilyan vester'),
    ('CUT        ch-685  (the cut across a right palm)',
     r'cut across it is ([a-z-]+) days old', lambda c: c - 685, spell, 'cut across'),
    ('ASH        ch-630  (a man in an ash)',
     r'ash[^.]{0,200}?for (a hundred and [a-z -]+?|one hundred and [a-z-]+?) days',
     lambda c: c - 630, aspell, 'in an ash'),
    ('REED       ch-629  (a woman in a reed)',
     r'reed[^.]{0,200}?for (a hundred and [a-z -]+?|one hundred and [a-z-]+?) days',
     lambda c: c - 629, aspell, 'in a reed'),
    ('BOY-DAYS   ch-653  (a boy of thirteen\'s own count)',
     # VOLUME 16 FIX, AND IT IS THE FINDING THIS SWEEP EXISTS FOR. THE ANCHOR
     # WAS `ch-701`, WHICH IS WHERE THE BOY'S COUNT STARTED IN VOLUME 15, AND
     # ON ARRIVAL IN VOLUME 16 IT REPORTED *10 ONE OUT* ON A BAND THAT WAS
     # CLEAN ON EVERY OTHER CATEGORY. THE BOY'S COUNT WAS RE-ANCHORED AT
     # `ch-653` IN VOLUME 15 AND EVERY CHAPTER OF 751-760 CARRIES THE
     # SUBTRACTION SPOKEN. A SWEEP THAT REPORTS A DEFECT BECAUSE A STATE FILE
     # WAS NEVER UPDATED IS NOT A SWEEP THAT HAS FOUND A DEFECT, AND IT IS
     # EXACTLY THE FAILURE OF `state/index.md` RULE 14 TURNED AROUND: A FIGURE
     # THAT WAS ONCE RIGHT AND THEN WENT STALE IS BETTER DRESSED THAN A FALSE
     # ONE, AND A TOOL THAT CARRIES A STALE ANCHOR REPORTED EITHER ONE.
     r'\b([a-z-]+) days\. \1 is ', lambda c: c - 653, spell, 'wat marshe'),
]


def speaker_text(path, who):
    """THE FIGURE A COUNTER OWES IS OWED BY ONE PERSON, AND TWO OF THE COUNTERS
    IN THIS VOLUME SHARE THE WORD *MORNINGS*: A MAN OF THIRTY-EIGHT COUNTS THE
    SHEET HE HAS READ OUT LOUD IN *MORNINGS* AND A MAN OF FIFTY-FOUR COUNTS THE
    MORNINGS HE HAS ASKED IN *MORNINGS*, AND A SEARCH OVER THE WHOLE CHAPTER
    COUNTS BOTH AND REPORTS FOUR FALSE 'ONE OUT' HITS IN A BAND THAT IS CLEAN.
    THE WINDOW IS THE CHARACTER-BLOCK PARAGRAPH THAT NAMES THE SPEAKER AND THE
    RUN OF QUOTED LINES THAT FOLLOWS IT."""
    lines = open(path, encoding='utf-8').read().splitlines()
    out = []
    for i, ln in enumerate(lines):
        if who in ln.lower() and not isq(ln):
            j = i + 1
            out.append(ln)
            while j < len(lines):
                if not lines[j].strip():
                    j += 1
                    if j < len(lines) and not isq(lines[j]):
                        break
                    continue
                if isq(lines[j]):
                    out.append(lines[j])
                    j += 1
                else:
                    break
            break
    return norm(' '.join(out))


def counters(lo, hi, vol='volume-16'):
    """EVERY COUNT A CHARACTER KEEPS ACROSS A BAND IS WRITTEN DOWN IN ORDER AND
    READ BACK.  A COUNTER THAT IS ONE OUT DOES NOT LOOK LIKE ONE OUT AND IT IS
    THE ONLY FIGURE IN THIS BOOK WITH NO ANCHOR TO CATCH IT.

    A MISSING FIGURE IS NOT A COUNTER ERROR.  A BOY OF THIRTEEN IS NOT ON THAT
    BANK EVERY MORNING, SO *THE FIGURE IS NOT ON THE PAGE* IS A PRESENCE
    QUESTION AND IS PRINTED AND NOT JUDGED.  A COUNTER IS ONE OUT ONLY WHEN THE
    EXPECTED FIGURE IS ABSENT AND A DIFFERENT FIGURE OF THE SAME UNIT IS ON THE
    PAGE IN ITS PLACE, AND THAT IS WHAT IS COUNTED HERE."""
    print(f'  THE LIVE COUNTERS, {lo}-{hi}, IN ORDER, READ BACK')
    bad = absent = 0
    for name, pat, rule, sp, who in COUNTERS:
        print(f'    {name}')
        for c in range(lo, hi + 1):
            p = f'chapters/{vol}/chapter-{c:04d}.md'
            raw = speaker_text(p, who) or norm(open(p, encoding='utf-8').read())
            want, n = rule(c), sp(rule(c))
            pats = pat if isinstance(pat, tuple) else (pat,)
            hits = []
            for pt in pats:
                hits += re.findall(pt, raw)
            got = [h for h in hits if h.strip() == n]
            present = bool(re.findall(who, raw)) or who in norm(open(p, encoding='utf-8').read())
            if got:
                print(f'      ch{c}: {want:4d}  {n:24s}  {len(got)} on the page')
            elif not present:
                absent += 1
                print(f'      ch{c}: {want:4d}  {n:24s}  --  not spoken in this morning '
                      f'({who} is not in this chapter)')
            elif hits:
                bad += 1
                print(f'      ch{c}: {want:4d}  {n:24s}  --  ONE OUT. page carries {hits}')
            else:
                absent += 1
                print(f'      ch{c}: {want:4d}  {n:24s}  --  not on this page '
                      f'(the speaker is not in this morning)')
    print(f'  COUNTERS: {bad} one out, {absent} not spoken in that morning.')
    return bad


if __name__ == '__main__':
    # REPAIRED AT THE REVIEW OF VOLUME 15 BAND 0005. THIS MAIN BLOCK USED TO
    # SWEEP THREE LITERAL RANGES AND IGNORE `sys.argv` ENTIRELY, SO
    # `batch-0004-arithmetic.py 741 750` PRINTED THE 731-740 BLOCK UNDER A
    # 741-750 NAME AND A READER HAD NO WAY OF TELLING. THE SWEEPS THEMSELVES
    # (`sweep`, `counters`) ALWAYS TOOK A RANGE AND ARE CORRECT; ONLY THE ENTRY
    # POINT LIED. THE CALIBRATIONS RUN FIRST AND ALWAYS, AND THE BAND TAKEN FROM
    # THE COMMAND LINE IS ANNOUNCED.
    # VOLUME 16 BAND 0001. THE VOLUME IS AN ARGUMENT NOW, BECAUSE A SCRIPT THAT
    # SWEEPS A RANGE AND HARDCODES THE DIRECTORY IT READS FROM WILL READ TEN
    # CHAPTERS OUT OF THE WRONG VOLUME AND PRINT A CLEAN ZERO, WHICH IS THE
    # WORST KIND OF WRONG, BECAUSE IT LOOKS LIKE A PASS. THE FOURTH ARGUMENT IS
    # THE VOLUME AND IT DEFAULTS TO THIS BAND'S OWN.
    band = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) >= 3 else (751, 760)
    vol = sys.argv[3] if len(sys.argv) >= 3 else 'volume-16'
    print(f'CALIBRATION 741-750, THEN 731-740, THEN THE BAND {band[0]}-{band[1]} '
          f'IN {vol}, WHICH IS THE RANGE AND THE VOLUME GIVEN ON THE COMMAND LINE:')
    print('CALIBRATION 741-750 (the last band certified 48 phrases, 0 flagged):')
    c1 = sweep(741, 750, 'volume-15')
    print('CALIBRATION 731-740 (the band before it certified 36 phrases, 0 flagged):')
    c2 = sweep(731, 740, 'volume-15')
    print(f'THE BAND {band[0]}-{band[1]}:')
    c3 = sweep(*band, vol=vol)
    print()
    print('THE COUNTER READ-BACK, CALIBRATED ON 741-750, WHICH THE LAST BAND CERTIFIED:')
    counters(741, 750, 'volume-15')
    print()
    counters(*band, vol=vol)
    print()
    print(f'SUMMARY: calibration 741-750 {c1}, 731-740 {c2}, '
          f'band {band[0]}-{band[1]} {c3}')
