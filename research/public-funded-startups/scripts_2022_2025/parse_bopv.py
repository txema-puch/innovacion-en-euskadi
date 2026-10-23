import re,sys,json
# usage: parse_bopv.py out.json txt...
out=[]
for fn in sys.argv[2:]:
    for l in open(fn,encoding='utf-8'):
        m=re.match(r'^\s*((?:EK|EKP|BE|BEK)[A-Z]*-\d{5}-(\d{4}))\s+(.+?)\s{2,}([\d\.]+,\d\d)\s*$',l.rstrip())
        if m: out.append(dict(exp=m.group(1),year=int(m.group(2)),name=m.group(3).strip().rstrip('.').strip(),amount=float(m.group(4).replace('.','').replace(',','.')),src=fn.split('/')[-1][:8]))
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
import collections
c=collections.defaultdict(lambda:[0,0])
for r in out: c[(r['src'],r['year'])][0]+=1; c[(r['src'],r['year'])][1]+=r['amount']
for k,v in sorted(c.items()): print(k,v)
