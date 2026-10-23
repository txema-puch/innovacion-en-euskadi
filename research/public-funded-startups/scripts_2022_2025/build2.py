import json,sys,os,re,csv,collections,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import base,slug
from sector import sector
W=sys.argv[1]
rows=json.load(open(f'{W}/cohort.json')); P=json.load(open(f'{W}/parsed.json'))
WEB=json.load(open(f'{W}/webcheck.json')) if os.path.exists(f'{W}/webcheck.json') else {}
MAN=json.load(open(f'{W}/manual.json')) if os.path.exists(f'{W}/manual.json') else {}
NOW=(2026,10,23)
def dt(s):
    m=re.match(r'(\d\d)/(\d\d)/(\d{4})',s or ''); return (int(m.group(3)),int(m.group(2)),int(m.group(1))) if m else None
def months(a,b=NOW): return (b[0]-a[0])*12+(b[1]-a[1])
def asc(s): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
hdr="name,cif,programme,year,public_amount_eur,sector,status,status_source,employees,employees_source,revenue_eur,revenue_year,revenue_source,private_funding_eur,funding_source,exit_or_valuation,notes,last_registry_act_date,last_registry_act_type,capital_increases,website_status,classification".split(',')
out=[]
for r in rows:
    id_=r['id']; p=P.get(id_,{}); E=p.get('em') or {}; I=p.get('ie') or {}; M=MAN.get(id_,{})
    notes=[f"id {id_}"]
    if r['exp']: notes.append(f"BOPV file {r['exp']}")
    if r['bdns_conv']: notes.append(f"BDNS call {r['bdns_conv']} award {r['bdns_date']}")
    if r.get('note'): notes.append(r['note'])
    if r['programme']=='SPRI Ekintzaile' and r['bdns_conv'] and not r['exp']: notes.append('not in BOPV list under this name (BOPV lists a natural-person promoter; BDNS records the company)')
    # identity checks
    cif=r['cif'] or I.get('cif') or ''
    def dd(a,b):
        a,b=dt(a),dt(b)
        if not a or not b: return None
        import datetime; return abs((datetime.date(*a)-datetime.date(*b)).days)
    if E and E.get('cif') and r['cif'] and E['cif']!=r['cif']:
        notes.append(f"empresia page {E.get('url')} has CIF {E['cif']} != {r['cif']}: match rejected"); E={}
    if E and E.get('cif') and (E['cif']==cif):
        notes.append('empresia match CIF-verified')
    elif E:
        gap=dd(E.get('const'),I.get('const')) if I else None
        import difflib
        en=asc(base(re.sub(r'\(.*?\)','',E.get('em_name',''))))
        same=max(difflib.SequenceMatcher(None,en,asc(base(x))).ratio() for x in [r['name'],r.get('name_bdns') or r['name']])>=0.85
        ft=asc(E.get('fulltext_names',''))
        if gap is not None and gap>(730 if same else 120):
            notes.append(f"empresia page '{E.get('em_name')}' incorporated {E.get('const')} vs infoempresa (CIF-verified) {I.get('const')}: different entity, empresia match rejected"); E={}
        elif not same:
            if asc(base(r['name'])) in ft and (gap is None or gap<=120):
                notes.append(f"registered name now {E.get('em_name')} (grant name appears in its BORME history)")
            else:
                notes.append(f"empresia name '{E.get('em_name')}' differs from grant name: match rejected"); E={}
    if M.get('em_reject'): E={}
    emurl=E.get('url',''); ieurl=I.get('url','')
    es=(E.get('status') or '').strip(); st='unknown'; src=''
    MAP={'ACTIVA':'active','EXTINGUIDA':'extinct','DISUELTA':'dissolved','CIERRE HOJA REGISTRAL':'dormant'}
    if es in MAP: st=MAP[es]; src=emurl
    elif I.get('status'):
        st={'Activa':'active','Disuelta':'dissolved','Extinguida':'extinct'}.get(I['status'],'unknown'); src=ieurl if st!='unknown' else ''
        if st=='unknown': notes.append(f"infoempresa status: {I['status']}")
    if st=='extinct' and E.get('status_date'): notes.append(f"extinguished {E['status_date']}")
    if st=='dormant': notes.append('registry sheet closed (cierre hoja registral)')
    if I.get('status') and es and I['status'].lower()[:4]!=es.lower()[:4] and not (es=='EXTINGUIDA' and I['status']=='Disuelta'): notes.append(f"infoempresa says {I['status']}")
    if E.get('concurso'): notes.append('BORME: insolvency (concurso) act(s): '+', '.join(sorted({a[1] for a in E['acts'] if 'concursal' in a[0].lower()})))
    if M.get('status'): st,src=M['status'],M['status_src']
    # dates
    const=dt(E.get('const') or I.get('const'))
    if const: notes.append(f"incorporated {const[2]:02d}/{const[1]:02d}/{const[0]}")
    incumbent = const and r['year']-const[0]>=4
    if r['programme'].endswith('Barne-Ekintzaile'):
        if incumbent: notes.append(f"incumbent parent ({r['year']-const[0]} yrs old at award): Barne-Ekintzaile funds intrapreneurship inside existing firms, so registry outcome reflects the parent, not the project")
        elif not const: notes.append('Barne-Ekintzaile beneficiary; age unknown (likely incumbent parent)')
    acts=sorted(E.get('acts',[]),key=lambda a:dt(a[1]) or (0,0,0),reverse=True)
    last_d,last_t=(acts[0][1],acts[0][0]) if acts else ('unknown','unknown')
    cap=E.get('cap_incr_dates',[]); ncap=E.get('n_cap_incr',0) if E else None
    capstr='unknown' if ncap is None else (str(ncap)+(f" ({'; '.join(cap)})" if cap else '')) 
    if E.get('capital'): notes.append(f"nominal capital {E['capital']}")
    CO=re.compile(r'(?i)\b(s\.?l\.?u?|s\.?a\.?|sl|sa|slu|coop|ltd|limited|llc|lcc|gmbh|corp|corporation|inc|ab|ou|srl|bv|fundacion|holding|group|company)\b')
    if E.get('owner') and CO.search(E['owner']): notes.append(f"sole shareholder (company) per empresia: {E['owner']}")
    elif E.get('owner'): notes.append('sole shareholder is a natural person (not named)')
    if E.get('addr'): notes.append(f"seat {E['addr']}")
    # employees/revenue
    emp=rev='unknown'; esrc=rsrc=''; ry='unknown'
    if st in ('active','acquired') and I.get('emp'):
        emp=I['emp'].replace('entre ','').replace(' empleados','').replace(' y ','-')+' (range)'; esrc=ieurl
        rev={'menos de 2 millones de euros':'<2000000 (range)'}.get(I.get('rev'),I.get('rev'))+('' if I.get('rev')=='menos de 2 millones de euros' else ' (range)'); rsrc=ieurl
    if I.get('acc_years'): ry=str(max(I['acc_years'])); notes.append(f"latest annual accounts on file at infoempresa: FY{ry} (years {','.join(map(str,sorted(I['acc_years'])))})")
    elif I: notes.append('no deposited annual accounts listed at infoempresa')
    if E.get('ventas') and E['ventas'] not in ('-',''): notes.append(f"empresia sales band {E['ventas']}")
    # website
    ws='none'; wnote=''
    cands=WEB.get(id_,[])
    good=[x for x in cands if x['brand'] and not x['parked'] and not (x['title'].lower().startswith('www.') and x['size']<2500)]
    if M.get('web'): ws=M['web']; wnote=M.get('web_note','') if ws!='none' else ''
    if M.get('web')=='none' and M.get('web_note'): notes.append('website: '+M['web_note'])
    elif good:
        g=sorted(good,key=lambda x:(x['firstword'],-(x['copy'] or 0)))[0]
        ws='live'; wnote=f"{g['final']} (title '{g['title'][:50]}'{', ©'+str(g['copy']) if g['copy'] else ''})"
    if wnote: notes.append('website: '+wnote)
    wcopy=None
    m=re.search(r'©(\d{4})',wnote); wcopy=int(m.group(1)) if m else None
    # classification
    sig_growth=[]; sig_life=[]
    if st=='active':
        for c in cap:
            if months(dt(c))<=24 and not (const and months(const,dt(c))<6): sig_growth.append(f'capital increase {c}')
        if emp!='unknown' and not emp.startswith('1-9'): sig_growth.append(f'employees {emp}')
        if rev not in ('unknown','<2000000 (range)'): sig_growth.append(f'revenue {rev}')
        cbatch=[a for a in acts if const and dt(a[1]) and months(const,dt(a[1]))>3]
        rec=[a for a in cbatch if months(dt(a[1]))<=36]
        if rec: sig_life.append(f'registry act {rec[0][1]} ({rec[0][0]})')
        if ws=='live' and (wcopy is None or wcopy>=2024): sig_life.append('live website')
        if ry!='unknown' and int(ry)>=2024: sig_life.append(f'annual accounts FY{ry} on file')
    if M.get('growth'): sig_growth.append(M['growth'])
    if st in ('extinct','dissolved','dormant'): cl='DEAD'
    elif st=='acquired' or M.get('absorbed'): cl='ABSORBED'
    elif st=='unknown': cl='UNCLEAR'
    elif sig_growth: cl='GROWING'
    elif sig_life: cl='OPERATING'
    else:
        if const and ((I and months(const)>=24) or (E and not I and months(const)>=36)): cl='ZOMBIE'
        else: cl='UNCLEAR'
    if st=='active' and any('concursal' in a[0].lower() and dt(a[1]) and months(dt(a[1]))<=36 for a in E.get('acts',[])): cl='ZOMBIE'; notes.append('classified ZOMBIE because the company is in insolvency proceedings (concurso) per BORME')
    if M.get('class'): cl=M['class']
    if sig_growth: notes.append('growth signals: '+'; '.join(sig_growth))
    elif sig_life: notes.append('life signals: '+'; '.join(sig_life))
    elif cl=='ZOMBIE': notes.append('no sign of life: no BORME act after the incorporation batch in the last 36 months, no annual accounts for FY2024+, no live website found')
    if M.get('note'): notes.append(M['note'])
    if emurl and src!=emurl: notes.append(f'registry acts, capital and objeto social from {emurl}')
    sec=M.get('sector') or sector(E.get('obj',''),r['name'])
    if E.get('obj'): notes.append('objeto social: '+E['obj'][:140])
    out.append(dict(name=r['name'],cif=cif or 'unknown',programme=r['programme'],year=r['year'],public_amount_eur=int(r['amount']) if r['amount']==int(r['amount']) else r['amount'],sector=sec,status=st,status_source=src or 'unknown',employees=emp,employees_source=esrc or 'unknown',revenue_eur=rev,revenue_year=ry,revenue_source=(rsrc or ieurl) if (rev!='unknown' or ry!='unknown') else 'unknown',private_funding_eur='unknown',funding_source='unknown',exit_or_valuation=M.get('exit','unknown'),notes='; '.join(notes),last_registry_act_date=last_d,last_registry_act_type=last_t,capital_increases=capstr,website_status=ws,classification=cl,_incumbent=bool(incumbent),_emurl=emurl))
with open(f'{W}/startups_2022_2025.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=hdr,extrasaction='ignore'); w.writeheader(); w.writerows(out)
json.dump(out,open(f'{W}/built.json','w'),ensure_ascii=False,indent=0)
C=collections.Counter
print(C((o['programme'],o['year']) for o in out))
print(C(o['status'] for o in out)); print(C(o['classification'] for o in out)); print(C(o['website_status'] for o in out))
