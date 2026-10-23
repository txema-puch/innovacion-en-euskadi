import json,sys,os,re,csv,collections,datetime
sys.path.insert(0,os.path.dirname(__file__)); from parsers import parse_em,strip_legal,parse_ie
W=sys.argv[1]; E=json.load(open(W+'/ents.json')); alias=json.load(open(W+'/em_alias.json')); MAN=json.load(open(W+'/manual_alias.json'))
web=json.load(open(W+'/web.json')) if os.path.exists(W+'/web.json') else {}
TODAY=datetime.date(2026,10,23); G24=datetime.date(2024,10,23); Z3=datetime.date(2023,10,23)
BASQUE_ONLY=('Gauzatu','DFB','DFG','BIC Gipuzkoa','Seed Capital','GCR','SPRI blog')
def d(s):
    try:
        if '-' in s: y,m,dd=s.split('-')
        else: dd,m,y=s.split('/')
        return datetime.date(int(y),int(m),int(dd))
    except Exception: return None
def sector(cnae,obj):
    c=cnae[:2] if cnae else ''
    M={'62':'Software/IT services','63':'Data/information services','58':'Software publishing','72':'R&D (scientific)','71':'Engineering/technical services','70':'Consulting','73':'Marketing/advertising','74':'Design/professional services','21':'Pharma','26':'Electronics','27':'Electrical equipment','28':'Machinery','25':'Metal products','24':'Metallurgy','22':'Rubber/plastics','20':'Chemicals','10':'Food','11':'Beverages','32':'Other manufacturing (incl. medical devices)','29':'Automotive','30':'Other transport equipment','35':'Energy','38':'Waste/recycling','46':'Wholesale trade','47':'Retail/e-commerce','85':'Education','86':'Health services','41':'Construction','43':'Construction (specialised)','33':'Repair/installation of machinery','23':'Non-metallic minerals','17':'Paper','18':'Printing','16':'Wood','13':'Textiles','14':'Apparel','31':'Furniture','61':'Telecoms','64':'Financial services','66':'Financial auxiliary','68':'Real estate','82':'Business support','93':'Sports/leisure','59':'Media/film','90':'Arts/creative','56':'Hospitality (food service)','01':'Agriculture','03':'Fishing/aquaculture','77':'Rental/leasing','80':'Security','52':'Logistics','49':'Transport'}
    return (M.get(c,'Other')+f' (CNAE {cnae[:4]})') if c else 'unknown'
rows=[]; stats=collections.Counter(); excluded=collections.Counter()
for e in E:
    progs=[x['prog'] for x in e['recs']]
    basque_prog=any(p.startswith(BASQUE_ONLY) for p in progs)
    bind_basque_flag=any('Basque' in (x.get('extra') or '') for x in e['recs'])
    if e['basque'] is False: excluded['registered outside Basque Country']+=1; continue
    if e['basque'] is None and not basque_prog and not bind_basque_flag: excluded['BIND, not matched to a Basque registry entity']+=1; continue
    s=alias.get(e['em_slug'],e['em_slug']); emurl=f'https://www.empresia.es/empresa/{s}/' if s else ''
    fn=f"{W}/dl/em/{s}.html"; o=parse_em(open(fn,errors='ignore').read()) if s and os.path.exists(fn) else None
    if o and not o['status']: o=None
    # sanity: if we had a CIF and empresia shows a different CIF, reject empresia match
    if o and e['cif'] and o.get('cif'):
        ec=o['cif'].replace('.','')
        if re.match(r'^[A-Z]\d{7}[A-Z0-9]$',ec) and ec[1:]!=e['cif'][1:]: o=None
        elif re.match(r'^[A-Z]\d{3,}$',ec) and not e['cif'].startswith(ec): o=None
    if o and not re.match(r'^[A-Z]\d{7}[A-Z0-9]$',o.get('cif','')): o['cif']=''
    name=(o['h1'] if o and o.get('h1') else '') or e['reg_name'] or (e['names'][0] if e['names'] else '')
    cif=e['cif'] or (o.get('cif') if o else '') or 'unknown'
    ieurl=('https://www.infoempresa.com'+e['uri']) if e['uri'] else ''
    notes=[]
    st='unknown'; ssrc='unknown'
    if o:
        ssrc=emurl
        st={'ACTIVA':'active','EXTINGUIDA':'extinct','DISUELTA':'dissolved','CIERRE HOJA REGISTRAL':'dormant'}.get(o['status'],o['status'].lower())
    ev=o['events'] if o else []
    lastd,lastt=(ev[0] if ev else ('',''))
    fus=[x for x in ev if re.search(r'(?i)fusi[oó]n|absorci',x[1])]
    caps=[x[0] for x in ev if x[1].startswith('Ampliación de capital')]
    ncap=o['n_cap_incr_badge'] if o else None
    w=web.get(e['em_slug'] or e['key'][1],[])
    live=[x for x in w if x['brand'] and not x['parked']]
    if live:
        x=live[0]; wst=f"live: {x['url']}"+(f" -> {x['final']}" if x['final'] and x['final'].rstrip('/')!=x['url'].rstrip('/') else '')+(f" (©{x['copy']})" if x['copy'] else '')
    elif w and any(x['parked'] for x in w): wst='domain parked/for sale: '+[x['url'] for x in w if x['parked']][0]
    elif e['em_slug'] in web: wst='no site found at guessed domains'
    else: wst='not checked'
    lpa=e.get('lpa'); la=(o.get('last_accounts') if o else '') or ''
    try: acc=max(int(la) if la.isdigit() else 0, int(lpa) if lpa else 0)
    except Exception: acc=int(la) if la.isdigit() else 0
    # classification
    recent_cap=[c for c in caps if d(c) and d(c)>=G24]
    sign=[]
    if lastd and d(lastd) and d(lastd)>=Z3: sign.append(f'BORME act {lastd}')
    if acc>=2023: sign.append(f'accounts filed for {acc}')
    if live and (live[0]['copy'] or 0)>=2024: sign.append('website ©'+str(live[0]['copy']))
    elif live: sign.append('website live')
    if not o:
        cls='UNCLEAR'
        if e['uri'] and lpa:
            st=f'unknown (registered; last accounts filed {lpa})'; ssrc='https://www.infoempresa.com/sugerencias?q='+(e['cif'] or e['names'][0]).replace(' ','%20')+' ; '+ieurl
            if int(lpa)>=2023: cls='OPERATING'; sign.append(f'accounts filed for {lpa} (infoempresa)')
            elif int(lpa)<=2022: cls='ZOMBIE'; sign=[]
    elif st in ('extinct','dissolved','dormant'):
        cls='ABSORBED' if fus else 'DEAD'
    elif recent_cap: cls='GROWING'
    elif sign: cls='OPERATING'
    else: cls='ZOMBIE'
    if fus and cls!='ABSORBED': notes.append('BORME merger act(s) while still active (likely absorber, not absorbed): '+'; '.join(f'{a} {b}' for a,b in fus[:3]))
    if cls=='ABSORBED': notes.append('BORME merger/absorption act(s): '+'; '.join(f'{a} {b}' for a,b in fus[:3])+' (direction absorber/absorbed not verified)')
    if cls=='GROWING': notes.append('capital increase(s) in last 24 months: '+', '.join(recent_cap))
    if cls in('OPERATING','ZOMBIE'): notes.append('signs of life: '+(', '.join(sign) if sign else 'none since 2023-10'))
    if o:
        notes.append(f"empresia: constituted {o.get('const') or 'n/a'}; CNAE {o.get('cnae') or 'n/a'}; nominal capital {o.get('capital') or 'n/a'}; ventas {o.get('ventas') or 'n/a'}; last accounts deposited {la or 'n/a'}; owner {o.get('owner') or 'n/a'}; seat {o.get('addr') or 'n/a'}")
        if o.get('status_date'): notes.append(f"{st} {o['status_date']}")
    if lpa: notes.append(f'infoempresa: last presented accounts {lpa}')
    if e['how'] and e['how'] not in ('cif',): notes.append('match: '+e['how'])
    if any(n in MAN for n in e['names']): notes.append('empresia entity chosen by hand from empresia search results (brand name differs from legal name)')
    if not o and not e['uri']: notes.append('not found in empresia/infoempresa (cooperative, very new, brand name differs, or not Basque)')
    elif not o: notes.append('infoempresa match but no empresia page resolved')
    for x in e['recs']:
        if x.get('extra'): notes.append('BIND page location: '+x['extra'])
    if any(p.startswith('Gauzatu') for p in progs):
        cd=d(o['const']) if o and o.get('const') else None; gy=min(int(x['year']) for x in e['recs'] if x['prog'].startswith('Gauzatu') and x['year'])
        if cd: notes.append(f"Gauzatu startup-age test: incorporated {cd.year}, first Gauzatu award {gy} -> {'YOUNG (≤5 yrs)' if gy-cd.year<=5 else 'ESTABLISHED (>5 yrs)'}")
    prog='; '.join(dict.fromkeys(progs)); yrs='; '.join(dict.fromkeys(str(x['year']) for x in e['recs'] if x['year']))
    amts=[float(x['amount']) for x in e['recs'] if x['amount'] not in ('',None)]
    amt=round(sum(amts),2) if amts else 'unknown'
    srcs=' ; '.join(dict.fromkeys(x['src'] for x in e['recs']))
    notes.insert(0,'programme sources: '+srcs)
    emp='unknown'; rev='unknown'; esrc='unknown'; ie_note=''
    iefn=f"{W}/dl/ie/{cif}.html"
    if os.path.exists(iefn) and os.path.getsize(iefn)>20000:
        io=parse_ie(open(iefn,errors='ignore').read())
        if io.get('ie_emp'):
            emp=io['ie_emp'].replace('entre ','').replace(' empleados','').replace(' y ','-')+' (range)'; esrc=ieurl
        if io.get('ie_status'): ie_note=f"infoempresa status: {io['ie_status']}"
        if io.get('ie_rev') and st=='active':
            rev={'menos de 2 millones de euros':'<2000000 (range)'}.get(io['ie_rev'],io['ie_rev']+' (range)')
    if rev=='unknown' and o and o.get('ventas') and st=='active': rev=f"{o['ventas']} (empresia 'ventas' band; bands seen: 0.5M, 1M, 2.5M)"
    if ie_note: notes.append(ie_note)
    rows.append(dict(name=name,cif=cif,programme=prog,year=yrs or 'unknown',public_amount_eur=amt,sector=sector(o.get('cnae','') if o else '',''),status=st,status_source=ssrc,employees=emp,employees_source=esrc,revenue_eur=rev,revenue_year=(la if rev!='unknown' and la else 'unknown'),revenue_source=((esrc if 'range' in rev else emurl) if rev!='unknown' else 'unknown'),private_funding_eur='unknown',funding_source='unknown',exit_or_valuation='unknown',notes='; '.join(notes),last_registry_act_date=lastd or 'unknown',last_registry_act_type=lastt or 'unknown',capital_increases=(ncap if ncap is not None else 'unknown'),website_status=wst,classification=cls))
# merge rows that resolved to the same empresia page (renamed companies listed under old and new names)
merged={}; order=[]
for r in rows:
    k=r['status_source'] if r['status_source'].startswith('https://www.empresia.es') else id(r)
    if k in merged:
        m=merged[k]
        for f in ('programme','year'):
            m[f]='; '.join(dict.fromkeys(m[f].split('; ')+r[f].split('; ')))
        if isinstance(m['public_amount_eur'],float) and isinstance(r['public_amount_eur'],float): m['public_amount_eur']=round(m['public_amount_eur']+r['public_amount_eur'],2)
        elif r['public_amount_eur']!='unknown' and m['public_amount_eur']=='unknown': m['public_amount_eur']=r['public_amount_eur']
        if m['cif']=='unknown': m['cif']=r['cif']
        if m['employees']=='unknown' and r['employees']!='unknown': m['employees'],m['employees_source']=r['employees'],r['employees_source']
        m['notes']+=' | merged duplicate listing: '+r['notes'][:300]
    else: merged[k]=r; order.append(k)
rows=[merged[k] for k in order]
hdr="name,cif,programme,year,public_amount_eur,sector,status,status_source,employees,employees_source,revenue_eur,revenue_year,revenue_source,private_funding_eur,funding_source,exit_or_valuation,notes,last_registry_act_date,last_registry_act_type,capital_increases,website_status,classification".split(',')
with open(W+'/startups_other.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=hdr); w.writeheader(); w.writerows(rows)
json.dump(dict(excluded=excluded),open(W+'/build_stats.json','w'))
print(len(rows),'excluded',dict(excluded))
print(collections.Counter(r['classification'] for r in rows)); print(collections.Counter(r['status'] for r in rows))
