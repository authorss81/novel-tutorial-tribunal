#!/usr/bin/env python3
"""Hand sweep for volume 21 band 2, 1011-1020. Read-only over chapters/."""
import re, sys, os, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(ROOT, "chapters", "volume-21")
DAYS = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]

o=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
t=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
HUND=['','one','two','three','four','five','six','seven','eight','nine']
h=['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
def ord2(n):
    base = num(n)
    if n % 100 not in (11,12,13) and n % 10 in (1,2,3,5,8,9):
        u={'one':'first','two':'second','three':'third','five':'fifth','eight':'eighth','nine':'ninth'}
        cut = max(base.rfind(' '), base.rfind('-'))
        return base[:cut+1] + u[base[cut+1:]]
    if base.endswith('y'): return base[:-1] + 'ieth'
    return base + 'th'
def weekword(n):
    if n < 100: return num(n)
    hd = HUND[n//100]                 # 'six'
    if n % 100: return "%s hundred and %s"%(hd, ord2(n%100))
    return "%s hundredth"%hd

def num(n):
    if n < 20: return o[n]
    if n < 100:
        r = t[n//10]
        return r+'-'+o[n%10] if n % 10 else r
    if n % 100 == 0: return h[n//100]
    return h[n//100]+' and '+num(n%100)

ORD = {1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh'}
ORDW={151:'hundred and fifty-first',152:'hundred and fifty-second',153:'hundred and fifty-third',
      154:'hundred and fifty-fourth',155:'hundred and fifty-fifth',156:'hundred and fifty-sixth',
      157:'hundred and fifty-seventh',158:'hundred and fifty-eighth',159:'hundred and fifty-ninth',
      160:'hundred and sixtieth'}
GORD={290:'ninetieth',291:'ninety-first',292:'ninety-second',293:'ninety-third',294:'ninety-fourth',
      295:'ninety-fifth',296:'ninety-sixth',297:'ninety-seventh',298:'ninety-eighth',299:'ninety-ninth'}

MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
SEASONS = ["spring","summer","autumn","fall","winter","springtime","summertime","wintertime"]
BANNED_WORDS = ["citizen","Veyra","System","panel","amendment","rail","brave","worth it","redeemed","forgiven","sorry","grateful","testimony","right of refusal"]
FORBIDDEN_CLASSES = {
  "MONTH": r"\b(" + "|".join(MONTHS) + r")\b",
  "SEASON": r"\b(" + "|".join(SEASONS) + r")\b",
}
RELATIVE_DAY = re.compile(r"\b(?:this|last|next|past|coming|that)\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b", re.I)
# a bare weekday NOT immediately preceded by "and it is a"/"and it is an" within the same sentence is fine;
# we flag all and read them.
BARE_DAY = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b")
HEADCOUNT = re.compile(r"\b(?:nine|eight|ten|seven|six|five|four|three|two|eleven|twelve|about nine|about eight|about ten)\s+(?:of\s+)?(?:them|people|men|women|persons|folks|ones there|of you)\b", re.I)
NUMWORD = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)"

WATER = {  # residue of ch upon eight
 3:("Four inches","about ninety of those ninety steps under","seven days"),
 4:("Eight inches","about eighty of those eighty-nine of those ninety steps under" if False else "about eighty of those ninety steps under","six days"),
 5:("Twelve inches","about seventy of those ninety steps under","five days"),
 6:("Sixteen inches","about sixty of those ninety steps under","four days"),
 7:("Sixteen inches","about sixty of those ninety steps under","three days"),
 0:("Sixteen inches","about sixty of those ninety steps under","two days"),
 1:("Sixteen inches","about sixty of those ninety steps under","one day"),
 2:("NONE","NONE","NONE"),
}

print("="*100)
print("A. CALENDAR AND COUNTERS, RUN FROM THE FORMULA, AND WHAT THE PAGE ACTUALLY CARRIES")
print("="*100)
files=[]
for ch in range(1011,1021):
    p=os.path.join(CH,"chapter-%d.md"%ch)
    if not os.path.exists(p):
        print("  MISSING %s"%p); continue
    files.append((ch,p))
    txt=open(p,encoding="utf-8").read()
    body="\n".join(txt.split("\n")[1:])
    shelf=ch-125; week=40+(ch-125)//7; day=(ch-125)%7+1
    fd=ch-283; fw,fl=divmod(fd,7)
    exp = {
      "weekday": DAYS[day-1],
      "weekphrase": "%s week"%weekword(week).replace("one hundred","hundred"),
      "morning": "His %s morning"%ord2(ch-250),
      "settle": num(ch-400),
      "division": num(ch-446),
      "door": num(ch-500),
      "kell": num(ch-554),
      "palm": num(ch-685),
      "offer_sub": "one thousand and %s less seven hundred"%num(ch-1000),
      "offer_fig": num(ch-700),
      "mistakes": "One %s wrong things"%ORDW[ch-860],
      "gravel_ord": "Two hundred and %s mornings of asking"%GORD[1+(ch-722)],
      "gravel_sub": "one thousand and %s less seven hundred and twenty-two, and then one"%(num(ch-1000)),
    }
    # boy subtraction: at 1001 the boy says "one thousand less six hundred and fifty-three" for 348
    exp["boy_sub"]="one thousand less %s"%num(1000-(ch-653))
    exp["gravel_sub"]="one thousand and %s less seven hundred and twenty-two, and then one"%num(ch-1000)
    miss=[]
    if "Wat Marshe is thirteen" not in txt: exp.pop("boy_sub", None)
    if "Wat Marshe is thirteen" in txt:
        for v in (num(ch-653), "one thousand less %s"%num(1000-(ch-653))):
            if v.lower() not in txt.lower(): miss.append("boy=%r"%v)
    for k,v in exp.items():
        if v.lower() not in txt.lower():
            miss.append("%s=%r"%(k,v))
    # fever
    dd = "day" if fl==1 else "days"
    fever_expect = ("The fever %s weeks old."%num(fw)) if fl==0 else ("The fever %s weeks and %s %s old."%(num(fw),num(fl),dd))
    if fever_expect.lower() not in txt.lower():
        miss.append("fever=%r"%fever_expect)
    # water
    wi,ws,wd = WATER[ch%8]
    if wi=="NONE":
        pass
    else:
        for v in (ws,wd):
            if v.lower() not in txt.lower(): miss.append("water=%r"%v)
    if miss:
        print("  ch %d  ** MISSING: %s"%(ch,"; ".join(miss)))
    else:
        print("  ch %d  all figures present and spelled as the formula gives them" % ch)

print()
print("="*100)
print("B. THE PALM FIGURE, IN THE DESCRIPTOR LINE AND IN THE SPEECH LINE -- BOTH PLACES, EVERY MORNING")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    want=num(ch-685)
    desc = "The cut across that palm is %s days old."%want
    speech_hits=len(re.findall(r"the cut across that palm is %s days old"%re.escape(want), txt, re.I))
    in_desc_line = desc.lower() in txt.lower()
    # descriptor line: the standalone paragraph "Ilyan Vester, thirty-one, nobody's, ..."
    m=re.search(r"Ilyan Vester, thirty-one, nobody.{0,4}s, and has been in this county [^\n]*\n", txt)
    descpara = m.group(0) if m else ""
    ok_desc = want in descpara
    ok_speech = speech_hits>=1
    print("  ch %d  want=%-28s descriptor-line=%s speech-line=%s (%d hits) %s"%(ch,want,ok_desc,ok_speech,speech_hits,"OK" if ok_desc and ok_speech else "** CHECK"))

print()
print("="*100)
print("C. RELATIVE NAMED DAYS -- HOUSE FIGURE ZERO, READ BY A PERSON AND NOT BY A GATE")
print("="*100)
total=0
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    body="\n".join(txt.split("\n")[1:])
    rel=[m.group(0) for m in RELATIVE_DAY.finditer(body)]
    total+=len(rel)
    if rel: print("  ch %d  ** %s"%(ch,rel))
print("  unanchored relative named-day phrases across the ten: %d"%total)

print()
print("="*100)
print("D. EVERY WEEKDAY MENTION, READ BY HAND -- EACH MUST CARRY ITS WEEK ORDINAl")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    body="\n".join(txt.split("\n")[1:])
    for sent in re.split(r"(?<=[.?!”])\s+", body):
        for m in BARE_DAY.finditer(sent):
            frag=sent[max(0,m.start()-90):m.end()+30].replace("\n"," ")
            print("  ch %d  ...%s..."%(ch,frag))

print()
print("="*100)
print("E. MONTHS (case-sensitive, word-bounded), SEASONS, AND THE BANNED WORD LIST")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    hits=[]
    for k,rx in FORBIDDEN_CLASSES.items():
        hits += ["%s:%r"%(k,m.group(0)) for m in re.finditer(rx,txt)]
    low=txt.lower()
    for w in BANNED_WORDS:
        if w.lower() in low: hits.append("BANNED:%s"%w)
    print("  ch %d  %s"%(ch, hits if hits else "clean"))

print()
print("="*100)
print("F. HEAD COUNTS OF PEOPLE, IN ANY WORDING")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    hits=[m.group(0) for m in HEADCOUNT.finditer(txt)]
    hits+= [m.group(0) for m in re.finditer(r"\babout\s+%s\b"%NUMWORD, txt)]
    print("  ch %d  %s"%(ch, hits if hits else "clean"))

print()
print("="*100)
print("G. 'four hundred' -- EVERY ONE MUST BE THE KELL FIGURE AND NOTHING ELSE")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    want=num(ch-554)
    for m in re.finditer(r"[Ff]our hundred and [^\s]+[^\s]*", txt):
        print("  ch %d  %-40s  KELL_WANTS=%s  %s"%(ch,m.group(0),want,"KELL" if m.group(0).lower()==want.lower() else "** NOT KELL"))

print()
print("="*100)
print("H. THE FIGURES THAT MAY NOT BE PRINTED -- the count of asking, the stitches, the age of a thing, the run-ordinals")
print("="*100)
pats = {
 "THIRTY-TWO NOTCHES / board age": r"board (?:is|has been|was) (?:about )?%s\b"%NUMWORD,
 "SIXTY-THREE": r"(?<!hundred and )sixty-three",
 "about N weeks": r"about %s weeks"%NUMWORD,
 "N times said": r"%s times"%NUMWORD,
 "second/third/fourth anchor": r"(?:second|third|fourth|fifth|sixth|seventh) (?:anchor|off-morning)",
 "three things left": r"\bthree things\b",
 "zero of new names": r"(?:no|not one) new name",
}
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    for k,rx in pats.items():
        for m in re.finditer(rx,txt,re.I):
            print("  ch %d  ** %s -> %r"%(ch,k,m.group(0)))
print("  (no line above this one means clean)")

print()
print("="*100)
print("I. 'thanked' -- EVERY OCCURRENCE MUST BE A REFUSAL, A NEGATION, OR A NAMING OF WHO IS NOT TO BE THANKED")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    for m in re.finditer(r"[Tt]hank\w*", txt):
        s=max(0,m.start()-140); e=min(len(txt),m.end()+60)
        print("  ch %d  ...%s..."%(ch,txt[s:e].replace("\n"," ")))

print()
print("="*100)
print("J. THE NOT-PULLED LINE -- REQUIRED IN EVERY CHAPTER OF THE BAND")
print("="*100)
NEED="Nothing on that landing was pulled, turned over, weighed in the hand, read aloud, carried inside, put back where it was, or used, and nobody laid a hand on that wood in order to take anything off it."
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    print("  ch %d  %s"%(ch,"present" if NEED in txt else "** ABSENT"))

print()
print("="*100)
print("K. DUPLICATE SENTENCES -- VERBATIM REPETITION INSIDE ONE CHAPTER, AND OPENING LINES ACROSS THE BAND")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    body="\n".join(txt.split("\n")[1:])
    sents=[s.strip() for s in re.split(r"(?<=[.?!”])\s+", body) if len(s.strip())>25]
    from collections import Counter
    for s,c in Counter(sents).items():
        if c>1: print("  ch %d  ** %d x  %r"%(ch,c,s[:90]))
        if c>5: print("  ch %d  ** OVER FIVE: %d x"%(ch,c))
print("  inside-chapter duplicates listed above (none = clean)")
opens=[]
for ch,p in files:
    lines=open(p,encoding="utf-8").read().split("\n")
    first=[l for l in lines[1:] if l.strip()][0]
    opens.append((ch,first[:60]))
    print("  ch %d  opens: %s"%(ch,first[:100]))
from collections import Counter
c=Counter(s for _,s in opens)
for s,n in c.items():
    if n>1: print("  ** TWO CHAPTERS OPEN ON THE SAME WORDS: %r"%s)

print()
print("="*100)
print("L. THE MIDPOINT, AND WHERE IT IS AND IS NOT")
print("="*100)
KEY=["rather have had the wrong","better for that piece of wood","wrong thing by the man who put it down"]
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    found=[k for k in KEY if k.lower() in txt.lower()]
    print("  ch %d  %s"%(ch,found if found else "—"))

print()
print("="*100)
print("M. THE OFFER, SPOKEN WITH THE SUBTRACTION, EVERY MORNING")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    fig=num(ch-700); sub="one thousand and %s less seven hundred"%num(ch-1000)
    print("  ch %d  figure %-22s %s | subtraction %-46s %s"%(ch,fig,"OK" if fig.lower() in txt.lower() else "** MISSING",sub,"OK" if sub.lower() in txt.lower() else "** MISSING"))

print()
print("="*100)
print("N. NOBODY ANSWERS A QUESTION ABOUT THAT NAME, AND NOBODY PUTS A NEW NAME ON ANYTHING")
print("="*100)
for ch,p in files:
    txt=open(p,encoding="utf-8").read()
    a = bool(re.search(r"[Nn]obody answered", txt))
    b = bool(re.search(r"[Nn]obody put a (new )?name on anything", txt))
    print("  ch %d  unanswered=%s  no-new-name=%s"%(ch,a,b))