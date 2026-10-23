import json,re,sys,unicodedata,difflib,collections
W=sys.argv[1]
bopv=json.load(open(f'{W}/bopv.json'))
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'\b(sociedad limitada( unipersonal| laboral)?|s\.?\s?l\.?\s?[lu]?\.?|s\.?\s?a\.?|s\.?\s?coop\.?|sociedad cooperativa|sl|slu|sll|sa)\b','',s)
    return re.sub(r'[^a-z0-9]','',s)
bd={2022:'787614',2023:'772515',2024:'769097'}
barne={2022:'783079',2023:'772453',2024:'769096'}
rows=[]
PT={}
EXTRA_LEGAL={'Olive Robotics, S.L','Bikaine Sport Supplements & Nutrition','Blue Reef Algae'}
for y,n in bd.items():
    awards=json.load(open(f'{W}/dl/bdns/ek_{n}.json'))['content']
    bp=[b for b in bopv if b['year']==y]
    used=set()
    for a in awards:
        cif,nm=a['beneficiario'].split(' ',1); nm=re.split(r',\s*ORGANIZATIONIDENTIFIER',nm)[0].strip()
        best=None;bs=0
        for i,b in enumerate(bp):
            if i in used: continue
            s0=difflib.SequenceMatcher(None,norm(nm),norm(b['name'])).ratio(); s=s0+(0.15 if abs(b['amount']-a['importe'])<1 and s0>=0.75 else 0)
            if s>bs: bs,best=s,i
        if best is not None and bs>0.75 and difflib.SequenceMatcher(None,norm(nm),norm(bp[best]['name'])).ratio()>=0.75: used.add(best); b=bp[best]
        else: b=None; print('NOMATCH',y,cif,nm,a['importe'],round(bs,2),bp[best]['name'] if best is not None else '')
        rows.append(dict(programme='SPRI Ekintzaile',year=y,cif=cif,name_bdns=nm,name=b['name'] if b else nm,exp=b['exp'] if b else '',amount=a['importe'],amount_bopv=b['amount'] if b else None,bdns_conv=n,bdns_date=a['fechaConcesion'],bopv=b['src'] if b else ''))
    persons=[b for i,b in enumerate(bp) if i not in used]
    for b in [p for p in persons if p['name'] in EXTRA_LEGAL]:
        rows.append(dict(programme='SPRI Ekintzaile',year=y,cif='',name_bdns='',name=b['name'],exp=b['exp'],amount=b['amount'],amount_bopv=b['amount'],bdns_conv='',bdns_date='',bopv=b['src'],note='in BOPV list but not in BDNS'))
    persons=[p for p in persons if p['name'] not in EXTRA_LEGAL]
    conv=[r for r in rows if r['year']==y and r['programme']=='SPRI Ekintzaile' and not r['exp']]
    PT[y]=dict(bopv_person_rows=len(persons),bopv_person_eur=sum(p['amount'] for p in persons),later_company_in_bdns=len(conv),later_company_eur=sum(r['amount'] for r in conv))
    print(y,'bdns',len(awards),'matched',len(used),'unmatched bopv',len(persons),sum(p['amount'] for p in persons))
    for p in persons: print('   P?',p['exp'],p['name'],p['amount'])
# 2025 from BOPV only
legal=re.compile(r'(?i)(S\.\s?Coop|S\.\s?L|S\.\s?A\.?$|Sociedad Limitada|Sociedad Anónima|Cooperativa|\bSL\b|\bSLU\b|Aie)')
for b in [b for b in bopv if b['year']==2025]:
    if legal.search(b['name']) or b['name'] in EXTRA_LEGAL: rows.append(dict(programme='SPRI Ekintzaile',year=2025,cif='',name_bdns='',name=b['name'],exp=b['exp'],amount=b['amount'],amount_bopv=b['amount'],bdns_conv='',bdns_date='',bopv=b['src']))
    else: print('   2025 P?',b['exp'],b['name'],b['amount']); PT.setdefault(2025,dict(bopv_person_rows=0,bopv_person_eur=0)); PT[2025]['bopv_person_rows']+=1; PT[2025]['bopv_person_eur']+=b['amount']
for y,n in barne.items():
    for a in json.load(open(f'{W}/dl/bdns/ek_{n}.json'))['content']:
        cif,nm=a['beneficiario'].split(' ',1); nm=re.split(r',\s*ORGANIZATIONIDENTIFIER',nm)[0].strip()
        rows.append(dict(programme='SPRI Barne-Ekintzaile',year=y,cif=cif,name_bdns=nm,name=nm,exp='',amount=a['importe'],amount_bopv=None,bdns_conv=n,bdns_date=a['fechaConcesion'],bopv=''))
cb=[r for r in rows if r['cif'].startswith('E')]
for r in cb: PT.setdefault('CB_'+r['programme']+str(r['year']),[0,0]); PT['CB_'+r['programme']+str(r['year'])][0]+=1; PT['CB_'+r['programme']+str(r['year'])][1]+=r['amount']
rows=[r for r in rows if not r['cif'].startswith('E')]
for i,r in enumerate(rows): r['id']=('EK' if r['programme'].endswith(' Ekintzaile') else 'BE')+str(r['year'])+'-'+str(i).zfill(3)
json.dump(rows,open(f'{W}/cohort.json','w'),ensure_ascii=False,indent=0)
json.dump(PT,open(f'{W}/persons.json','w'),indent=1); print(PT)
print(len(rows),collections.Counter((r['programme'],r['year']) for r in rows))
