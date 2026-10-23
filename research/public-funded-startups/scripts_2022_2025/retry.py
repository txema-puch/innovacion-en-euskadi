import json,sys,os,subprocess,time,re,urllib.parse
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import base,slug,txt
rows={r['id']:r for r in json.load(open(sys.argv[1]))}; P=json.load(open(sys.argv[2])); out=sys.argv[3]
ALT=json.load(open(sys.argv[4]))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def get(u,fn):
    r=subprocess.run(['curl','-sL','-m','30','-A',UA,'-o',fn,'-w','%{http_code}',u],capture_output=True,text=True).stdout
    time.sleep(1.2); return r
def emok(fn):
    t=open(fn,'rb').read().decode('utf-8','ignore'); return 'ESTADO' in t and 'Resultados de la b' not in t[:3000] and 'No hay resultados' not in t
only=sys.argv[5].split(',') if len(sys.argv)>5 else None
for id_,r in rows.items():
    if only and id_ not in only: continue
    if r['cif'][:1] in 'GJF' or 'coop' in r['name'].lower(): continue
    p=P.get(id_,{})
    names=list(dict.fromkeys([base(x) for x in ALT.get(id_,[])+[r['name'],r.get('name_bdns') or r['name']]]))
    if not p.get('em'):
        fn=f"{out}/{id_}_em.html"; done=False
        for n in names:
            for u in [f"https://www.empresia.es/empresa/{slug(n)}/",f"https://www.empresia.es/busqueda/?q={urllib.parse.quote_plus(n)}"]:
                c=get(u,fn)
                if c=='200' and emok(fn): done=True; print(id_,'em',u,flush=True); break
                if c=='200' and 'busqueda' in u:
                    links=list(dict.fromkeys(re.findall(r'href="/empresa/([a-z0-9-]+)/"',open(fn,'rb').read().decode('utf-8','ignore'))))
                    cand=[l for l in links if l.startswith(slug(n)[:12])]
                    if cand:
                        u2=f"https://www.empresia.es/empresa/{cand[0]}/"; c=get(u2,fn)
                        if c=='200' and emok(fn): done=True; print(id_,'em',u2,'(from search)',flush=True); break
            if done: break
        if not done: print(id_,'em MISS',names,flush=True); os.path.exists(fn) and os.remove(fn)
    if not p.get('ie'):
        fn=f"{out}/{id_}_ie.html"; done=False
        for n in names:
            for x in ['sl','slu','sll','slp','sa','sad','sal','sociedad-limitada']:
                u=f"https://www.infoempresa.com/es-es/es/empresa/{slug(n)}-{x}"; c=get(u,fn)
                if c=='200':
                    t=open(fn,'rb').read().decode('utf-8','ignore'); m=re.search(r'empresaCif:\s*"([A-Z0-9]*)"',t); cif=m.group(1) if m else ''
                    if not r['cif'] or cif in ('',r['cif']): done=True; print(id_,'ie',u,cif,flush=True); break
            if done: break
        if not done: print(id_,'ie MISS',flush=True); os.path.exists(fn) and os.remove(fn)
