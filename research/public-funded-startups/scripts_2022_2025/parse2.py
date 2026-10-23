import json,sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import txt
rows=json.load(open(sys.argv[1])); d=sys.argv[2]
DH=re.compile(r'^\d{1,2} de \w+ de \d{4}$')
def em(fn):
    raw=open(fn,'rb').read().decode('utf-8','ignore')
    t=txt(fn); o={}
    if 'ESTADO' not in t or 'Resultados de la b' in t[:2000]: return None
    m=re.search(r'<link rel="canonical" href="([^"]+)"',raw); o['url']=m.group(1) if m else ''
    m=re.search(r'ESTADO\s*\n?\s*([A-ZÁÉÍÓÚ ]+?)\s*(?:\((\d\d/\d\d/\d{4})\))?\s*\n',t); o['status']=m.group(1).strip() if m else ''
    m=re.search(r'\((?:Extinguida|Disuelta)[^\d]{0,10}(\d\d/\d\d/\d{4})\)',t); o['status_date']=m.group(1) if m else ''
    m=re.search(r'Empresa\s*ESTADO\s*[A-Z ]+?\s*\n(?:\(?[\d/]+\)?\s*\n)?([^\n]+)',t); o['em_name']=m.group(1).strip() if m else ''
    m=re.search(r'CIF\s+([A-Z]\d{7}[A-Z0-9])',t); o['cif']=m.group(1) if m else ''
    m=re.search(r'\n((?:https?://)?www\.[a-z0-9\-\.]+\.[a-z]{2,6}[^\s]*)\s*\n',t[:6000]); o['web']=m.group(1) if m else ''
    m=re.search(r'Objeto social\s*([^\n]{0,220})',t); o['obj']=m.group(1).strip() if m else ''
    m=re.search(r'Fecha constituci[oó]n\s*(\d\d/\d\d/\d{4})',t); o['const']=m.group(1) if m else ''
    m=re.search(r'Capital social\s*([\d\.,]+ ?€)',t); o['capital']=m.group(1) if m else ''
    m=re.search(r'Ventas\s*([^\n]{0,20})',t); o['ventas']=m.group(1).strip() if m else ''
    m=re.search(r'Últimas cuentas depositadas\s*([^\n]{0,20})',t); o['last_accounts']=m.group(1).strip() if m else ''
    m=re.search(r'Propietario\s*([^\n]{0,80})',t); o['owner']=m.group(1).strip() if m else ''
    m=re.search(r'\n([^\n]*?\([A-ZÁÉÍÓÚÑ\-\s/]+\))\.?\s*Ver mapa',t); o['addr']=m.group(1).strip() if m else ''
    m=re.search(r'Ampliación de capital\.\s*(\d+)\s*\n',t); o['n_cap_incr']=int(m.group(1)) if m else 0
    m=re.search(r'Filtro aplicado:(.*?)(Informes comerciales Axesor|RESUMEN BORME)',t,re.S); blk=m.group(1) if m else ''
    acts=[];cur=None;boundary=False
    L=[x.strip() for x in blk.split('\n') if x.strip()]
    own=re.sub(r'\s*\(.*?\)','',o.get('em_name','')).strip()
    for i,l in enumerate(L):
        if DH.match(l): boundary=True; continue
        if l.startswith('Fecha inscripci'):
            dm=re.search(r'(\d\d/\d\d/\d{4})',l)
            if cur and dm: acts.append((cur,dm.group(1)))
            cur=None; boundary=True; continue
        if boundary and len(l)<70 and l[-1] in '.:' and not l.startswith('Publicaci'): cur=l.rstrip('.:'); boundary=False; continue
        if l.startswith('Publicación de la empresa'):
            pub=l[len('Publicación de la empresa'):].strip(' :')
            if not pub and i+1<len(L): pub=L[i+1].strip(' :')
            pub=re.sub(r'\s*:.*$','',pub).strip()
            if pub!=own: cur=None
        boundary=False
    o['acts']=acts
    o['fulltext_names']=t[:200000]
    o['cap_incr_dates']=sorted({a[1] for a in acts if a[0].startswith('Ampliación de capital')},key=lambda x:x[6:]+x[3:5]+x[:2])
    o['concurso']=any('concursal' in a[0].lower() for a in acts)
    return o
def ie(fn):
    raw=open(fn,'rb').read().decode('utf-8','ignore'); t=txt(fn); o={}
    m=re.search(r'empresaCif:\s*"([A-Z0-9]+)"',raw); o['cif']=m.group(1) if m else ''
    m=re.search(r'availableYears:\s*\[([\d,\s]*)\]',raw); ys=[int(x) for x in re.findall(r'\d{4}',m.group(1))] if m else []; o['acc_years']=ys
    m=re.search(r'<link rel="canonical" href="([^"]+)"',raw); o['url']=m.group(1) if m else ''
    m=re.search(r'Su situación mercantil actual es ([^\n\.]+?) y su CIF',t); o['status']=m.group(1) if m else ''
    m=re.search(r'cuenta con ([^\n]*?empleados)[^\n]*?facturación anual de ([^\n]+?)\.',t)
    if m: o['emp'],o['rev']=m.group(1),m.group(2)
    m=re.search(r'Fecha de constitución\s*\n\s*(\d\d/\d\d/\d{4})',t); o['const']=m.group(1) if m else ''
    m=re.search(r'último anuncio en el BORME ha sido publicado el (\d\d/\d\d/\d{4})',t); o['last_borme']=m.group(1) if m else ''
    return o
res={}
for r in rows:
    o={}
    for k,f in (('em',em),('ie',ie)):
        fn=f"{d}/{r['id']}_{k}.html"
        if os.path.exists(fn) and os.path.getsize(fn)>5000:
            try: o[k]=f(fn)
            except Exception as e: o[k]={'err':str(e)}
    res[r['id']]=o
json.dump(res,open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
