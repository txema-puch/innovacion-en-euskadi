import json,sys,os,re,html,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import base
rows={r['id']:r for r in json.load(open(sys.argv[1]))}; hits=sys.argv[2]; d=sys.argv[3]
PARK=re.compile(r'(?i)(domain (is )?for sale|dominio (está )?en venta|buy this domain|this domain (name )?(is|may be) for sale|parked|sedo|dan\.com|afternic|hugedomains|godaddy|domain has expired|dominio ha caducado|coming soon|under construction|en construcci[oó]n|website is under|cuenta suspendida|account suspended|default web page|plesk|it works!|welcome to nginx|index of /|página no disponible)')
def asc(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
out={}
for l in open(hits):
    p=l.split()
    if len(p)<4: continue
    id_,dom,code,eff=p[0],p[1],p[2],p[3]
    fn=f"{d}/{id_}__{dom}.html"
    if not os.path.exists(fn): continue
    raw=open(fn,'rb').read().decode('utf-8','ignore')
    m=re.search(r'(?is)<title[^>]*>(.*?)</title>',raw); title=html.unescape(m.group(1)).strip()[:90] if m else ''
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    words=[w for w in re.findall(r'[a-z0-9]+',asc(base(rows[id_]['name']))) if len(w)>2]
    tl=asc(t+' '+title); joined=''.join(words)
    brand = joined in re.sub(r'[^a-z0-9]','',tl) or (len(words)>=1 and all(w in tl for w in words))
    yrs=[int(y) for y in re.findall(r'(?:©|&copy;|copyright|\(c\))\s*(?:[a-z\s\.,]{0,30})?(20[0-2]\d)(?:\s*[-–]\s*(20[0-2]\d))?',raw,re.I) for y in y if y] if False else []
    for m in re.finditer(r'(?i)(?:©|&copy;|copyright)[^<]{0,60}',raw):
        yrs+= [int(y) for y in re.findall(r'20[0-2]\d',m.group(0))]
    parked=bool(PARK.search(t[:3000]+title)) and len(t)<6000
    out.setdefault(id_,[]).append(dict(domain=dom,final=eff,title=title,brand=brand,parked=parked,copy=max(yrs) if yrs else None,size=len(t),firstword=dom.split('.')[0]!=joined))
json.dump(out,open(sys.argv[4],'w'),ensure_ascii=False,indent=0)
n=0
for k,v in sorted(out.items()):
    good=[x for x in v if x['brand'] and not x['parked']]
    if good: n+=1
    for x in v: print(k,rows[k]['name'][:35],'|',x['domain'],'->',x['final'][:50],'|',x['title'][:50],'| brand',x['brand'],'parked',x['parked'],'©',x['copy'],'size',x['size'])
print('companies with brand-verified live site:',n,file=sys.stderr)
