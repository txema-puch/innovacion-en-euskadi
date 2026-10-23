import sys,re,html,json
def txt(fn):
    b=open(fn,'rb').read().decode('utf-8','ignore')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b); b=re.sub(r'<[^>]+>','\n',b); b=html.unescape(b)
    return re.sub(r'[ \t]+',' ',re.sub(r'\s*\n\s*','\n',b))
def parse(fn):
    t=txt(fn); o={}
    if 'Resultados de b' in t[:300]: return None
    m=re.search(r'ESTADO\s*\n?\s*([A-ZÁÉÍÓÚ ]+?)\s*(?:\((\d\d/\d\d/\d{4})\))?\s*\n',t); o['status']=m.group(1).strip() if m else ''; o['status_date']=m.group(2) if m and m.group(2) else ''
    m=re.search(r'\((?:Extinguida|Disuelta) el (\d\d/\d\d/\d{4})\)',t); 
    if m: o['status_date']=m.group(1)
    m=re.search(r'\n([^\n]*?\([A-ZÁÉÍÓÚÑ\-\s/]+\))\.?\s*Ver mapa',t); o['addr']=m.group(1).strip() if m else ''
    m=re.search(r'Objeto social\s*([^\n]{0,200})',t); o['obj']=m.group(1).strip() if m else ''
    m=re.search(r'Capital social\s*([\d\.,]+ ?€)',t); o['capital']=m.group(1) if m else ''
    m=re.search(r'Ampliación de capital\.\s*(\d+)',t); o['n_cap_incr']=int(m.group(1)) if m else 0
    incs=[int(x.replace('.','')) for x in re.findall(r'Aumento de capital:\s*\|?\s*([\d\.]+) €',t)]
    o['sum_cap_incr_shown']=sum(incs)
    m=re.findall(r'Cambio de denominaci[oó]n[^\n]*\n([^\n]{0,160})',t); o['name_changes']=m[:2]
    dates=re.findall(r'Fecha inscripción: (\d\d/\d\d/\d{4})',t)
    o['last_borme']=dates[0] if dates else ''; o['first_borme']=dates[-1] if dates else ''
    for k in ['Disolución','Extinción','Declaración concursal','Situación concursal','Cierre provisional','Fusión','Absorción','Transformación']:
        o['act_'+k]=len(re.findall(k,t))
    m=re.search(r'Últimas cuentas depositadas\s*([^\n]{0,20})',t); o['last_accounts']=m.group(1) if m else ''
    m=re.search(r'Socio único[^\n]*\n([^\n]{0,100})',t); o['socio_unico']=m.group(1) if m else ''
    return o
if __name__=='__main__':
    for f in sys.argv[1:]: print(f,json.dumps(parse(f),ensure_ascii=False))
