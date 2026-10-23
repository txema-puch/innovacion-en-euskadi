import json,re,csv,sys,unicodedata
S=sys.argv[1]
rows=json.load(open(f"{S}/ek2021.json")); ie=json.load(open(f"{S}/extract.json"))
em={}
for l in open(f"{S}/em_all.txt"):
    f,j=l.split(' ',1); em.setdefault(f[:13],json.loads(j) if j.strip()!='null' else None)
def slug(s): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
def base(n): return re.sub(r'(?i),?\s*(S\.\s?Coop\.?|S\.L\.L\.|S\.L\.U\.|S\.\s?L\.?|S\.\s?A\.?|Aie|Sociedad Limitada)\s*$','',n).strip()
LF={'s.l.':'sl','s.l.l.':'sll','s.l.u.':'slu','s.a.':'sa','aie':'aie','sociedad limitada':'sociedad-limitada'}
sector={'EK-00001-2021':'Industrial waste recycling','EK-00002-2021':'Digital health (physio rehab software)','EK-00003-2021':'Software (health XR)','EK-00005-2021':'Interactive communication tech (holography)','EK-00006-2021':'Engineering/tech products','EK-00008-2021':'unknown','EK-00010-2021':'Nutrition tech','EK-00017-2021':'Industrial cleaning (dry ice)','EK-00018-2021':'Software/videogames','EK-00021-2021':'R&D engineering','EK-00023-2021':'Media production (podcasts)','EK-00024-2021':'Digital design files (automotive 3D parts)','EK-00026-2021':'Hardware (delivery systems)','EK-00027-2021':'Data/smart-city','EK-00029-2021':'Digital health software','EK-00030-2021':'Hardware (drones/boards)','EK-00031-2021':'Monitoring/analytics','EK-00032-2021':'Electronics/semiconductors','EK-00033-2021':'Software/marketing','EK-00034-2021':'Renewable energy (solar pumping)','EK-00035-2021':'Food (infant/dietetic)','EK-00036-2021':'Digital health (physiotherapy)','EK-00037-2021':'unknown','EK-00038-2021':'Biotech/pharma','EK-00040-2021':'Aquaculture','EK-00041-2021':'unknown','EK-00045-2021':'Data/hosting','EK-00049-2021':'unknown','EK-00050-2021':'Energy projects','EK-00051-2021':'Distributed energy','EK-00052-2021':'Engineering/product design','EK-00053-2021':'Power electronics (corporate)','EK-00054-2021':'Software','EK-00055-2021':'Construction','EK-00056-2021':'Software (cognitive training)','EK-00058-2021':'Software (app)','EK-00059-2021':'Sporting goods (fishing)','EK-00064-2021':'unknown','EK-00066-2021':'unknown','EK-00070-2021':'Esports/sports','EK-00072-2021':'Research','EK-00074-2021':'Metal stamping/industrial','EK-00075-2021':'Agri-genetics/cannabis R&D','EK-00076-2021':'Acoustic insulation manufacturing','EK-00077-2021':'SaaS (maintenance/energy efficiency)','EK-00087-2021':'Textiles (innovative)','EK-00088-2021':'Hospitality (coffee)','EK-00089-2021':'Industrial valves','EK-00091-2021':'Data analytics/training','EK-00092-2021':'Consulting/R&D projects','EK-00093-2021':'VR for hospitals','EK-00094-2021':'Cosmetics R&D','EK-00096-2021':'IT services','EK-00100-2021':'Medical devices','EK-00109-2021':'Plastics recycling (WEEE)','EK-00110-2021':'Engineering (water treatment)','EK-00111-2021':'Biotech (cosmetics)','EK-00113-2021':'unknown','EK-00114-2021':'unknown','EK-00115-2021':'E-commerce','EK-00116-2021':'Industrial fabrication (finned tube)','EK-00117-2021':'Racing simulators','EK-00120-2021':'Containers (eco)','EK-00121-2021':'Food products','EK-00127-2021':'Tech applications'}
web={'EK-00002-2021':'https://trak.es/ (redirects to clinicatrak.com, ©2026 TrakPhysio)','EK-00010-2021':'https://nutrenaissance.com/','EK-00026-2021':'https://normo.es/ (©2026)','EK-00027-2021':'https://www.whiteholedata.com/ (©2021-2024)','EK-00036-2021':'https://fisify.com/','EK-00038-2021':'https://nanokide.com/','EK-00052-2021':'https://weetbe.com/','EK-00055-2021':'https://qerqus.com/ (©2025)','EK-00056-2021':'https://www.impulsocognitivo.com/','EK-00076-2021':'https://www.acustrain.com/es/','EK-00077-2021':'https://satiins.es/','EK-00093-2021':'https://vrpharma.io/ (©2026)','EK-00100-2021':'https://www.inmedicaltherapeutics.com/ (©2026)','EK-00109-2021':'https://induplastrecycling.com/ (©2026)','EK-00110-2021':'https://ceataingenieria.com/','EK-00111-2021':'https://optidelbiosystems.com/ (©2026)','EK-00117-2021':'https://levitty.com/ (©2023)','EK-00053-2021':'https://www.gamesaelectric.com/'}
extra_notes={
'EK-00038-2021':'Website states "Nanokide Therapeutics is now part of Hermes Lifescience"; deal terms not public. BORME entity still ACTIVA.',
'EK-00089-2021':'paravalves.com now serves an Arnett Valves (US) page; relationship (acquisition/distribution/domain resale) unverified.',
'EK-00053-2021':'Corporate subsidiary (Gamesa Electric), not a startup; included because it is in the official Ekintzaile 2021 list.',
'EK-00051-2021':'S.A. with 1.28M EUR nominal capital at/after founding; likely corporate-backed venture, not a classic startup.',
'EK-00074-2021':'300k EUR nominal capital; likely industrial/corporate venture.',
'EK-00049-2021':'Candidate match: empresia "BASQUE PAY PSC" (Getxo, crypto services, ACTIVA, 5 capital increases) https://www.empresia.es/empresa/basque-pay-psc/ - identity not confirmed, so status left unknown.',
'EK-00041-2021':'Candidate match: empresia "IPSUM RD SOLUTIONS" (Barakaldo BIC Ezkerraldea, ACTIVA) https://www.empresia.es/empresa/ipsum-rd-solutions/ - identity not confirmed.',
'EK-00113-2021':'Cooperative: registered in the Basque Cooperatives Register, not the Registro Mercantil/BORME, so free BORME-derived sites do not cover it.',
'EK-00114-2021':'Cooperative: registered in the Basque Cooperatives Register, not BORME; not found.',
'EK-00008-2021':'No exact match found on empresia/infoempresa.','EK-00066-2021':'No exact match found on empresia/infoempresa.',
'EK-00018-2021':'Infoempresa: Concursal (insolvency); empresia: CIERRE HOJA REGISTRAL.',
'EK-00070-2021':'480k EUR nominal capital after 2 capital increases, yet registry sheet closed; freakcontrol.com domain for sale.',
'EK-00072-2021':'Extinct 17/12/2021, the same year it received the grant; neure.com domain for sale.',
}
hdr="name,cif,programme,year,public_amount_eur,sector,status,status_source,employees,employees_source,revenue_eur,revenue_year,revenue_source,private_funding_eur,funding_source,exit_or_valuation,notes".split(',')
out=[]
for r in rows:
    if not (r['entity'] or r['name'] in ('Nutrenaissance','Impulso Cognitivo')): continue
    e=r['exp']; b=base(r['name']); legal=r['name'][len(b):].strip(' ,').lower()
    ieurl=f"https://www.infoempresa.com/es-es/es/empresa/{slug(b)}-{LF.get(legal,'sl')}"
    emurl=f"https://www.empresia.es/empresa/{slug(b)}/"
    if e=='EK-00094-2021': ieurl="https://www.infoempresa.com/es-es/es/empresa/labei-cosmetics-sl"
    I=ie.get(e,{}) or {}; E=em.get(e) or {}
    if e=='EK-00049-2021': E={}
    st='unknown'; src=''; notes=[f"BOPV file {e}"]
    es=(E.get('status') or '').strip()
    if es=='ACTIVA': st='active'; src=emurl
    elif es=='EXTINGUIDA': st='extinct'; src=emurl; notes.append(f"extinguished {E.get('status_date')}")
    elif es=='DISUELTA': st='dissolved'; src=emurl
    elif es=='CIERRE HOJA REGISTRAL': st='dormant'; src=emurl; notes.append('BORME: registry sheet closed (cierre hoja registral), typically after tax deregistration or failure to file accounts')
    elif I.get('ie_status')=='Disuelta': st='dissolved'; src=ieurl
    elif I.get('ie_status')=='Activa': st='active'; src=ieurl
    if e=='EK-00038-2021': st='acquired'; src='https://nanokide.com/ ; '+emurl
    if I.get('ie_status') and es and I['ie_status'].lower()[:4]!=es.lower()[:4] and not (es=='EXTINGUIDA' and I['ie_status']=='Disuelta'):
        notes.append(f"Infoempresa says {I['ie_status']}")
    emp='unknown'; esrc=''; rev='unknown'; rsrc=''
    if st in('active','acquired') and I.get('ie_emp'):
        emp=I['ie_emp'].replace('entre ','').replace(' empleados','').replace(' y ','-')+' (range)'; esrc=ieurl
        rev={'menos de 2 millones de euros':'<2000000 (range)','más de 50 millones de euros':'>50000000 (range)'}.get(I.get('ie_rev'),I.get('ie_rev')); rsrc=ieurl
    if E:
        notes.append(f"BORME via empresia: nominal capital {E.get('capital') or 'n/a'}; {E.get('n_cap_incr',0)} capital increase(s); BORME acts {E.get('first_borme')}..{E.get('last_borme')}; seat {E.get('addr') or 'n/a'}")
    if e in web: notes.append('website live: '+web[e])
    if e in extra_notes: notes.append(extra_notes[e])
    exitv='Acquired by Hermes Lifescience (terms not public)' if e=='EK-00038-2021' else 'unknown'
    out.append(dict(name=r['name'],cif=I.get('cif') or 'unknown',programme='SPRI Ekintzaile',year=2021,public_amount_eur=int(r['amount']) if r['amount']==int(r['amount']) else r['amount'],sector=sector.get(e,'unknown'),status=st,status_source=src or 'unknown',employees=emp,employees_source=esrc or 'unknown',revenue_eur=rev,revenue_year='unknown',revenue_source=rsrc or 'unknown',private_funding_eur='unknown',funding_source='unknown',exit_or_valuation=exitv,notes='; '.join(notes)))
with open(f"{S}/startups.csv",'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=hdr); w.writeheader(); w.writerows(out)
import collections
print(len(out),collections.Counter(o['status'] for o in out))
print('amount cohort',sum(float(o['public_amount_eur']) for o in out))
