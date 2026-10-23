import json,sys,os,re,collections
sys.path.insert(0,os.path.dirname(__file__)); from parsers import strip_legal,norm,slug
W=sys.argv[1]; R=json.load(open(W+'/recs_m.json'))
BASQ=('ARABA','ALAVA','BIZKAIA','VIZCAYA','GIPUZKOA','GUIPUZCOA')
ents=collections.OrderedDict()
for r in R:
    m=r['match']
    if m and m['cif']: k=('cif',m['cif'])
    elif r['cif']: k=('cif',r['cif'])
    else: k=('nm',norm(strip_legal(r['name'])))
    e=ents.setdefault(k,dict(key=list(k),names=[],cif=(m['cif'] if m else r['cif']) or '',reg_name=(m['name'] if m else ''),uri=(m['uri'] if m else ''),city=(m['city'] if m else ''),lpa=(m['lpa'] if m else None),how=r['how'],recs=[]))
    if r['name'] and r['name'] not in e['names']: e['names'].append(r['name'])
    e['recs'].append({k2:r[k2] for k2 in ('prog','year','amount','src','extra')})
    if m and not e['uri']: e.update(reg_name=m['name'],uri=m['uri'],city=m['city'],lpa=m['lpa'],cif=m['cif'] or e['cif'])
for e in ents.values():
    e['basque']=any(b in e['city'] for b in BASQ) if e['city'] else None
    nm=e['reg_name'] or (e['names'][0] if e['names'] else '')
    e['em_slug']=slug(strip_legal(re.sub(r'\s*\(.*\)$','',nm))) if nm else ''
json.dump(list(ents.values()),open(W+'/ents.json','w'),ensure_ascii=False,indent=0)
E=list(ents.values()); print(len(E), collections.Counter((bool(e['uri']),e['basque']) for e in E))
print('multi-programme',sum(1 for e in E if len(set(x['prog'].split(' (')[0].split(' –')[0] for x in e['recs']))>1))
