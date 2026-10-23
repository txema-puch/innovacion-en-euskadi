import json,sys,os,re,hashlib,collections
sys.path.insert(0,os.path.dirname(__file__)); from parsers import strip_legal,norm,qkey
W=sys.argv[1]; recs=json.load(open(W+'/recs.json'))
BASQ={'ARABA','ALAVA','ARABA/ALAVA','ALAVA/ARABA','BIZKAIA','VIZCAYA','GIPUZKOA','GUIPUZCOA'}
def sug(q):
    fn=W+'/dl/sug/'+hashlib.md5(q.encode()).hexdigest()+'.json'
    if not os.path.exists(fn): return []
    d=json.load(open(fn))['resp'].get('data') or {}
    out=[]
    for c in (d.get('1') or []):
        m=re.match(r'^([A-Z]\d{7}[A-Z0-9])\s+(.*)$',c['name'])
        cif,nm=(m.group(1),m.group(2)) if m else ('',c['name'])
        out.append(dict(cif=cif,name=nm,uri=c['uri'],city=(c.get('ciudad') or '').upper(),lpa=c.get('last_presented_account'),q=q))
    return out
def isbasq(c): return any(b in c['city'] for b in BASQ)
res=[]
for r in recs:
    q=r['cif'] if r['cif'] else qkey(r['name'])
    cands=sug(q); m=None; how=''
    if r['cif']:
        m=next((c for c in cands if c['cif']==r['cif']),None); how='cif' if m else ''
        if not m and r['name']:
            q=qkey(r['name']); cands=sug(q)
            ex=[c for c in cands if norm(qkey(c['name']))==norm(q)]
            if ex: m=ex[0]; how='name-fallback(cif-not-indexed)'
    else:
        nq=norm(q)
        ex=[c for c in cands if norm(qkey(c['name']))==nq]
        exb=[c for c in ex if isbasq(c)]
        if len(exb)>=1: m=exb[0]; how='exact-name-basque'
        elif len(ex)==1: m=ex[0]; how='exact-name'
        elif len(ex)>1: m=ex[0]; how='exact-name-ambiguous'
        else:
            coop=bool(re.search(r'(?i)coop|koop|s\.?c\.?l',r['name']))
            sw=[c for c in cands if isbasq(c) and len(nq)>=4 and norm(c['name']).startswith(nq) and (not coop or re.search(r'(?i)coop|koop',c['name']))]
            if len(sw)==1: m=sw[0]; how='prefix-basque'
            elif len(sw)>1: how='prefix-ambiguous:'+'|'.join(c['name'] for c in sw[:4])
    r['match']=m; r['how']=how
json.dump(recs,open(W+'/recs_m.json','w'),ensure_ascii=False,indent=0)
c=collections.Counter((r['prog'].split(' (')[0].split(' –')[0], 'M' if r['match'] else 'none', (isbasq(r['match']) if r['match'] else None)) for r in recs)
for k,v in sorted(c.items(),key=str): print(k,v)
