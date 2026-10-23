import json,sys,os,subprocess,time,re,urllib.parse
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import base,suffix,slug
rows=json.load(open(sys.argv[1])); out=sys.argv[2]; site=sys.argv[3]
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def get(u,fn):
    r=subprocess.run(['curl','-sL','-m','30','-A',UA,'-o',fn,'-w','%{http_code} %{url_effective}',u],capture_output=True,text=True).stdout.split(' ',1)
    time.sleep(1.2); return r[0], (r[1] if len(r)>1 else '')
log=open(os.path.join(out,f'fetch_{site}.log'),'a')
for r in rows:
    if r['cif'][:1] in ('G','J','F') or 'coop' in r['name'].lower(): continue
    b=base(r['name']); 
    if site=='em':
        fn=os.path.join(out,f"{r['id']}_em.html")
        if os.path.exists(fn) and os.path.getsize(fn)>20000: continue
        u=f"https://www.empresia.es/empresa/{slug(b)}/"; c,eff=get(u,fn)
        ok=c=='200' and 'Resultados de b' not in open(fn,'rb').read()[:3000].decode('utf-8','ignore') and 'ESTADO' in open(fn,'rb').read().decode('utf-8','ignore')
        if not ok:
            u=f"https://www.empresia.es/busqueda/?q={urllib.parse.quote_plus(b)}"; c,eff=get(u,fn)
        print(r['id'],c,eff,file=log,flush=True)
    else:
        fn=os.path.join(out,f"{r['id']}_ie.html")
        if os.path.exists(fn) and os.path.getsize(fn)>20000: continue
        sfx=suffix(r['name']); order=[sfx]+[x for x in ['sl','slu','sll','sa'] if x!=sfx]
        hit=None
        for x in order:
            u=f"https://www.infoempresa.com/es-es/es/empresa/{slug(b)}-{x}"; c,eff=get(u,fn)
            if c=='200':
                t=open(fn,'rb').read().decode('utf-8','ignore'); m=re.search(r'empresaCif:\s*"([A-Z0-9]+)"',t)
                cif=m.group(1) if m else ''
                if not r['cif'] or cif==r['cif']: hit=(u,cif); break
                os.rename(fn,fn+f'.{x}.mismatch')
        if not hit and os.path.exists(fn): os.remove(fn)
        print(r['id'],hit,file=log,flush=True)
