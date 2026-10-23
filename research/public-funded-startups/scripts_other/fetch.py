import json,sys,re,unicodedata,subprocess,os,time
rows=json.load(open(sys.argv[1])); out=sys.argv[2]
extra={'Nutrenaissance','Impulso Cognitivo'}
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-'); return s
def base(n):
    return re.sub(r'(?i),?\s*(S\.\s?Coop\.?|S\.L\.L\.|S\.L\.U\.|S\.\s?L\.?|S\.\s?A\.?|Aie|Sociedad Limitada)\s*$','',n).strip()
for i,r in enumerate(rows):
    if not (r['entity'] or r['name'] in extra): continue
    b=base(r['name']); full=r['name']
    legal=full[len(b):].strip(' ,').lower()
    lf={'s.l.':'sl','s.l.l.':'sll','s.l.u.':'slu','s.a.':'sa','s. coop.':'s-coop','aie':'aie','sociedad limitada':'sociedad-limitada'}.get(legal,'sl')
    cands={'ie':f"https://www.infoempresa.com/es-es/es/empresa/{slug(b)}-{lf}",'em':f"https://www.empresia.es/empresa/{slug(b)}/"}
    for k,u in cands.items():
        fn=os.path.join(out,f"{r['exp']}_{k}.html")
        if os.path.exists(fn) and os.path.getsize(fn)>20000: continue
        code=subprocess.run(['curl','-sL','-m','30','-A',UA,'-o',fn,'-w','%{http_code}',u],capture_output=True,text=True).stdout
        print(r['exp'],k,code,u,flush=True); time.sleep(1.5)
