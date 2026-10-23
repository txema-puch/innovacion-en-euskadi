import json,re,glob,os,sys
W=sys.argv[1]; recs=[]
def add(name,cif,prog,year,amount,src,extra=''):
    recs.append(dict(name=name.strip(),cif=(cif or '').strip(),prog=prog,year=year,amount=amount,src=src,extra=extra))
# Gauzatu
months={}
for f in glob.glob(W+'/dl/bopv/sum/*.month'): pass
gzmap={'1501097a':'2015/03','1600304a':'2016/01','1700448a':'2017/01','1800489a':'2018/01','1901044a':'2019/02','2000663a':'2020/02','2100425a':'2021/01','2200613a':'2022/02','2205803a':'2022/12'}
for o in json.load(open(W+'/gz.json')):
    nm=re.sub(r'\s{2,}',', ',o['name'])
    add(nm,o.get('cif',''),'Gauzatu-Industria (Basque Gov., reimbursable advance)',o['year'],o['amount'],f"https://www.euskadi.eus/bopv2/datos/{gzmap[o['rid']]}/{o['rid']}.pdf")
# Bizkaia
area={'680654':1,'680655':2,'701647':2,'740080':1,'740090':2,'740096':4,'770297':1,'770416':2,'804568':1,'804569':2,'804571':4,'835008':1,'835010':2,'878819':1,'878820':2,'878825':4,'878827':5}
an={1:'Área 1 proyectos empresariales innovadores',2:'Área 2 nuevas empresas innovadoras',4:'Área 4 aceleración',5:'Área 5 programas de aceleración'}
persons={}
for n,a in area.items():
    for c in json.load(open(f'{W}/dl/bdns/conc_{n}.json'))['content']:
        b=c['beneficiario']; m=re.match(r'^([A-Z]\d{7}[A-Z0-9])\s+(.*)$',b)
        if m and m.group(1)[0] in 'ABFGJNUVW':
            add(m.group(2),m.group(1),f'DFB Creación de Empresas Innovadoras – {an[a]}',int(c['fechaConcesion'][:4]),c['importe'],f'https://www.infosubvenciones.es/bdnstrans/api/concesiones/busqueda?vpd=GE&numeroConvocatoria={n}&pageSize=500')
        else: persons[('DFB',a)]=persons.get(('DFB',a),0)+1
# Gipuzkoa
gip=json.load(open(W+'/gip_all.json'))
for r in gip:
    d=r.get('Descripción','')
    if 'TXEKINTEK' in d or 'BARNETEKIN' in d:
        p='DFG creación EBTs – TXEKINTEK' if 'TXEKINTEK' in d else 'DFG creación EBTs – BARNETEKIN (intrapreneurship)'
        b=r['Beneficiario']
        if re.match(r'^[ABFGJNUVW]\d{7}[A-Z0-9]$',b): add('',b,p,int(r['Fecha de concesión'][:4]),float(r['Importe']),'https://api.gipuzkoairekia.eus/dataset/recurso/3d443361-614d-44e4-a845-dce3ce3b8da4/descargar')
        else: persons[('DFG',p)]=persons.get(('DFG',p),0)+1
# BIC Gipuzkoa
for l in open(W+'/bicgip_raw.txt'):
    s=l.strip()
    if not s or s.startswith('TE AYUDAMOS'): break
    if s in ('BioTech Foofs',): s='BioTech Foods'
    add(s,'','BIC Gipuzkoa incubated (empresas impulsadas)','','','https://bicgipuzkoa.eus/empresas-impulsadas/')
# BIND
bw={1:'20190916220813',2:'20190916230651',3:'20190916222838',4:'20200921134744',5:'20210923054803',6:'20220817143956',7:'20231206211423'}
ed_year={1:2016,2:2017,3:2018,4:2019,5:2020,6:2021,7:2022,8:2023}
for o in json.load(open(W+'/bind.json')):
    if o['name']=='[...]': continue
    nth={1:'1st',2:'2nd',3:'3rd'}.get(o['edition'],f"{o['edition']}th")
    add(o['name'],'',f"BIND 4.0 (SPRI) edition {o['edition']}",ed_year[o['edition']],'',f"https://web.archive.org/web/{bw[o['edition']]}/https://bind40.com/area/{nth}-edition/",extra=o['based'])
for nm,c in [('4i Intelligent Insights','Spain'),('Aunoa','Spain'),('Detektia','Spain'),('Eatamigo','Spain'),('Recog Analytics','Spain'),('We are clickers','Spain'),('Uktena','Spain'),('Uali','Spain'),('Hedro Sistemas Inteligentes','Spain'),('Goldilock','United Kingdom'),('Safeloc Systems','Spain'),('Orbik Cybersecurity','Spain'),('Infinite Foundry','Portugal'),('Visionaries 777','Singapore'),('Acceleration Robotics','Spain'),('Advanced Algorithms 4 Radar','Spain'),('51toCarbonZero','United Kingdom'),('Gundo','Spain'),('Kernova','Spain'),('Nawattia','Spain')]:
    add(nm,'','BIND 4.0 (SPRI) edition 8',2023,'','https://web.archive.org/web/20240413002113/https://bind40.com/2024/01/26/25-open-innovation-projects-via-bind-4-0-in-2024/',extra=c)
# Seed Capital Bizkaia (named logos only; BAF = fund-of-funds holdings excluded)
scb={'fondo i':['AI Power','Boletus Pay','Citiservi','MyFleet','Hermeneus','Talantia','Teccam','Jeekjee','Barbara IoT','Innitius','Mikrobiomik','Fastbase Solutions','Addilan','Alterity','Herko','Innomy','AOTECH','Nantek','Zuma','Nymiz','Aresar','Zetrack','Emicasolar','Yoid','Puzztime','Revenant B-Traz','Puntodis','Nneat'],
     'fondo bi':['BeGas','Biotermiak','Histocell','Lookiero','Satlantis','WAT','Smartbrands','Osteophoenix','Egoin','Idertia','Biolid','ADI Abanto','Pine'],
     'feis':['Insulclock','Koiki','Ubikare','Urbegi','APlanet','Lamia','Coometas','Siwa Clinic','Revenant','Suspertu','Biocarbon'],
     'start':['Roble Academy','Landatu','Adressless','Neu Current','Seenapse','Oreka','Odei.io','Code Contract'],
     'konfekoop':['Cibersare','Gaztaroa Sartu','Gertuko','Grip-on','Matrelle','Gurekin','Copy Astarloa','Leartiker','Coopenor','Barrenetxe']}
for f,l in scb.items():
    for nm in l: add(nm,'',f'Seed Capital Bizkaia ({f.title()})','','','https://www.seedcapitalbizkaia.eus/portfolio/')
# GCR (press, SPRI blog)
for nm,u in [('Inmedical Therapeutics','https://www.spri.eus/es/blog/emprendimiento/inmedical-therapeutics-cierra-una-ronda-de-800-000e-con-la-entrada-de-viscofan-y-gestion-de-capital-riesgo-del-pais-vasco-del-grupo-spri-y-el-asesoramiento-de-elkargi/'),('Optidel Biosystems','https://www.spri.eus/es/blog/financiacion/fondos-de-capital-riesgo/optidel-biosystems-recibe-el-respaldo-de-inversores-de-capital-riesgo/'),('Multiverse Computing','https://www.spri.eus/es/blog/financiacion/fondos-de-capital-riesgo/multiverse-computing-consolida-a-euskadi-como-referente-europeo-en-software-cuantico-e-inteligencia-artificial/'),('Oncomatryx','https://www.spri.eus/es/blog/financiacion/fondos-de-capital-riesgo/kutxa-fundazioa-el-gobierno-vasco-y-el-gobierno-de-espana-impulsan-la-transformacion-de-oncomatryx-en-biofarmaceutica/'),('Orbik Cybersecurity','https://www.spri.eus/es/blog/financiacion/fondos-de-capital-riesgo/orbik-cybersecurity-consolida-su-crecimiento-y-anuncia-una-nueva-fase-de-expansion-hasta-2030/'),('USA Group','https://www.spri.eus/es/blog/financiacion/fondos-de-capital-riesgo/usa-group-da-un-nuevo-impulso-a-su-crecimiento-con-la-incorporacion-de-nuevos-socios/')]:
    lab='GCR public VC (SPRI blog names Gestión de Capital Riesgo del País Vasco)' if nm not in ('Multiverse Computing','Oncomatryx') else 'SPRI blog "fondos de capital riesgo" category (GCR not named in post text)'
    add(nm,'',lab,'','',u)
add('InspectRail','','GCR public VC – BasqueTek Ventures (SPRI blog)','','','https://www.spri.eus/es/blog/financiacion/la-tecnologia-ferroviaria-de-inspectrail-obtiene-un-respaldo-de-15-millones-en-financiacion/')
json.dump(recs,open(W+'/recs.json','w'),ensure_ascii=False,indent=0)
import collections
print(len(recs)); print(collections.Counter(r['prog'].split(' (')[0].split(' –')[0] for r in recs)); print('persons',persons)
