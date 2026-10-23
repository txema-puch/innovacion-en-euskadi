import re,sys,json,glob,os
# Gauzatu-Industria BOPV annex: "Name   amount" lines; year from 'AÑO YYYY' or 'ejercicio YYYY'
out=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.txt')):
    t=open(f,encoding='utf-8',errors='ignore').read()
    m=re.search(r'(?:A[ÑN]O|EJERCICIO)\s+(20\d\d)',t) or re.search(r'durante (?:el ejercicio )?(20\d\d)',t)
    yr=int(m.group(1)) if m else None
    rid=os.path.basename(f)[:-4]
    prev=''
    for l in t.splitlines():
        s=l.rstrip()
        mm=re.match(r'^\s*(\S.*?)\s{2,}([\d\.]+,\d\d)\s*$',s)
        if mm:
            name=mm.group(1).strip()
            if prev and not re.search(r'(?i)(S\.\s?L\.?|S\.\s?A\.?|Coop\.?|S\.L\.L\.|S\.L\.U\.|Sociedad)\s*,?\s*$',prev) and False: pass
            out.append(dict(rid=rid,year=yr,name=name,amount=float(mm.group(2).replace('.','').replace(',','.'))))
            prev=''
        else:
            prev=s.strip() if s.strip() else prev
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
import collections
c=collections.Counter((o['rid'],o['year']) for o in out); print(c)
print(sum(o['amount'] for o in out))
