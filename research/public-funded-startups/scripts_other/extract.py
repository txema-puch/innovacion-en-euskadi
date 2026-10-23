import json,sys,re,os,html
sys.path.insert(0,'')
rows=json.load(open(sys.argv[1])); d=sys.argv[2]
def txt(fn):
    if not os.path.exists(fn): return ''
    b=open(fn,'rb').read().decode('utf-8','ignore')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b); b=re.sub(r'<[^>]+>','\n',b); b=html.unescape(b)
    return re.sub(r'\s*\n\s*','\n',b)
res={}
for r in rows:
    e=r['exp']; ie=txt(f"{d}/{e}_ie.html"); em=txt(f"{d}/{e}_em.html")
    if not ie and not em: continue
    o={'name':r['name']}
    m=re.search(r'Su situación mercantil actual es ([^\n\.]+?) y su CIF es ([A-Z]\d{7}[A-Z0-9])',ie)
    if m: o['ie_status'],o['cif']=m.group(1),m.group(2)
    else:
        m=re.search(r'CIF ([A-Z]\d{7}[A-Z0-9])',ie); o['cif']=m.group(1) if m else ''
    m=re.search(r'cuenta con ([^\n]*?empleados)[^\n]*?facturación anual de ([^\n]+?)\.',ie)
    if m: o['ie_emp'],o['ie_rev']=m.group(1),m.group(2)
    m=re.search(r'<title>|^(.*)$',ie[:300]); 
    o['ie_title']=ie.strip().split('\n')[0][:90]
    o['em_title']=em.strip().split('\n')[0][:90]
    m=re.search(r'ESTADO\n?([A-ZÁÉÍÓÚ ]+)(?:\s*\((\d\d/\d\d/\d{4})\))?',em); 
    if m: o['em_status']=(m.group(1).strip(),m.group(2))
    m=re.search(r'Ventas\n?([^\n]+)',em); o['em_sales']=m.group(1) if m else ''
    m=re.search(r'(?i)Emplead[oa]s\n?([^\n]{0,40})',em); o['em_emp']=m.group(1) if m else ''
    m=re.search(r'(?i)(Domicilio social|Domicilio)\n?([^\n]{0,80})',em); o['em_addr']=m.group(2) if m else ''
    m=re.search(r'(?i)Objeto social\n?([^\n]{0,160})',em); o['em_obj']=m.group(1) if m else ''
    m=re.search(r'(?i)(Fecha de constituci[oó]n|Constituci[oó]n)\n?([^\n]{0,20})',em); o['em_const']=m.group(2) if m else ''
    res[e]=o
json.dump(res,open(sys.argv[3],'w'),ensure_ascii=False,indent=1)
for e,o in res.items(): print(e,'|',o.get('name'),'|',o.get('cif'),'|',o.get('ie_status'),'|',o.get('em_status'),'|',o.get('ie_emp'),'|',o.get('ie_rev'),'|',o.get('em_sales'),'|',o.get('em_emp'))
