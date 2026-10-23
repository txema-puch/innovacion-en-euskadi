import json,sys,os,re,subprocess,html,unicodedata
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__)); from parsers import strip_legal,parse_em
W=sys.argv[1]; E=json.load(open(W+'/ents.json')); alias=json.load(open(W+'/em_alias.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def a(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
stop={'technologies','technology','solutions','solution','the','company','europe','iberia','data','health','media','systems','delivery','innovation','app','labs','industrial','grupo','talleres','sistemas','ingenieria','soluciones','basque','spain','energy','bio','smart','digital','global','advanced'}
def emactive(e):
    s=alias.get(e['em_slug'],e['em_slug']); fn=f"{W}/dl/em/{s}.html"
    if not s or not os.path.exists(fn): return None
    o=parse_em(open(fn,errors='ignore').read()); return o and o['status']=='ACTIVA'
def cands(e):
    names=[strip_legal(re.sub(r'\s*\(.*\)$','',n)) for n in e['names']]+([strip_legal(re.sub(r'\s*\(.*\)$','',e['reg_name']))] if e['reg_name'] else [])
    out=[]
    for n in names:
        w=re.findall(r'[a-z0-9]+',a(n))
        if not w: continue
        out.append(''.join(w))
        if len(w)>1 and w[0] not in stop and len(w[0])>3: out.append(w[0])
        if len(w)>1: out.append('-'.join(w))
    return list(dict.fromkeys(out))[:4]
def probe(e):
    key=e['em_slug'] or e['key'][1]
    res=[]
    for c in cands(e):
        for tld in ['com','es','eus','io']:
            u=f"https://{c}.{tld}/"; fn=f"{W}/dl/web/{key}__{c}.{tld}.html"
            r=subprocess.run(['curl','-sL','-4','-m','12','-A',UA,'-o',fn,'-w','%{http_code} %{url_effective}',u],capture_output=True,text=True).stdout.split()
            if r and r[0]=='200' and os.path.getsize(fn)>800:
                t=open(fn,'rb').read().decode('utf-8','ignore')
                m=re.search(r'(?is)<title[^>]*>(.*?)</title>',t); title=html.unescape(m.group(1)).strip()[:80] if m else ''
                yrs=[int(y) for y in re.findall(r'(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(20\d\d)',t,re.I)]
                parked=bool(re.search(r'(?i)domain (is )?for sale|dominio.*venta|buy this domain|parked|sedo|dan\.com|hugedomains|godaddy',t[:20000]))
                brand=c.split('-')[0][:6] in a(t)
                res.append(dict(url=u,final=r[1] if len(r)>1 else '',title=title,copy=max(yrs) if yrs else None,parked=parked,brand=brand))
            else:
                try: os.remove(fn)
                except: pass
        if any(x['brand'] and not x['parked'] for x in res): break
    return key,res
todo=[e for e in E if e['basque'] is not False and (e['em_slug']) and emactive(e) is not False]
out={}
with ThreadPoolExecutor(10) as ex:
    for k,r in ex.map(probe,todo): out[k]=r
json.dump(out,open(W+'/web.json','w'),indent=0,ensure_ascii=False)
print('done',len(todo),sum(1 for v in out.values() if any(x['brand'] and not x['parked'] for x in v)))
