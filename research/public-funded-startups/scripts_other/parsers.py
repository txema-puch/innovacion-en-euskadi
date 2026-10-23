import re,html,unicodedata
def txt(b):
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b); b=re.sub(r'<[^>]+>','\n',b); b=html.unescape(b)
    return re.sub(r'[ \t]+',' ',re.sub(r'\s*\n\s*','\n',b))
def slug(s): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
def norm(s): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
LEGAL=r'(?i)[,\s]+(SOCIEDAD LIMITADA LABORAL|SOCIEDAD LIMITADA|SOCIEDAD ANONIMA|S\.?\s?L\.?\s?L\.?|S\.?\s?L\.?\s?U\.?|S\.?\s?L\.?\s?P\.?|S\.?\s?L\.?|S\.?\s?A\.?\s?L\.?|S\.?\s?A\.?\s?U\.?|S\.?\s?A\.?|S\.?\s?Coop\.?( Pequeña)?|Sdad\.? Coop\.?|KOOP\.? ELK\.?( TXIKIA)?|S COOP( PEQUEÑA)?|A\.?I\.?E\.?)\s*$'
def strip_legal(n):
    n=re.sub(r'\s*\(.*?\)\s*$','',n.strip())
    for _ in range(2): n=re.sub(LEGAL,'',n).strip(' ,.')
    return n
def parse_em(b):
    t=txt(b); o={}
    if 'Resultados de b' in t[:400]: return None
    m=re.search(r'ESTADO\s*\n?\s*([A-ZÁÉÍÓÚ ]+?)\s*(?:\((\d\d/\d\d/\d{4})\))?\s*\n',t); o['status']=m.group(1).strip() if m else ''
    m=re.search(r'\((?:Extinguida|Disuelta) el (\d\d/\d\d/\d{4})\)',t); o['status_date']=m.group(1) if m else ''
    m=re.search(r'Objeto social\s*([^\n]{0,200})',t); o['obj']=m.group(1).strip() if m else ''
    m=re.search(r'Capital social\s*([\d\.,]+ ?€)',t); o['capital']=m.group(1) if m else ''
    m=re.search(r'\n([^\n]*?\([A-ZÁÉÍÓÚÑ\-\s/]+\))\.?\s*Ver mapa',t); o['addr']=m.group(1).strip() if m else ''
    for k,lab in [('cnae',r'CNAE'),('cif',r'CIF'),('const',r'Fecha constituci[oó]n'),('ventas',r'Ventas'),('registro',r'Registro'),('last_accounts',r'[ÚU]ltimas cuentas depositadas'),('owner',r'Propietario'),('organ',r'[ÓO]rgano administraci[oó]n')]:
        m=re.search(r'\n'+lab+r'\s*\n?([^\n]{1,120})',t) if k!='cnae' else re.search(r'\nCNAE ([^\n]{1,120})',t)
        o[k]=m.group(1).strip() if m else ''
    ev=re.findall(r'<time class="icon" datetime="(\d{4}-\d\d-\d\d)".*?<h3>([^<]+)</h3>',b,re.S)
    o['events']=[(d,html.unescape(h).strip(' .:')) for d,h in ev]
    m=re.search(r'Ampliación de capital\.\s*<span class="badge">(\d+)',b); o['n_cap_incr_badge']=int(m.group(1)) if m else 0
    m=re.search(r'<h1[^>]*>(.*?)</h1>',b,re.S); o['h1']=html.unescape(re.sub('<[^>]+>','',m.group(1))).strip() if m else ''
    return o
def parse_ie(b):
    t=txt(b); o={}
    m=re.search(r'Su situación mercantil actual es ([^\n\.]+?) y su CIF es ([A-Z]\d{7}[A-Z0-9])',t)
    if m: o['ie_status'],o['cif']=m.group(1),m.group(2)
    else:
        m=re.search(r'CIF:?\s*([A-Z]\d{7}[A-Z0-9])',t); o['cif']=m.group(1) if m else ''
    m=re.search(r'cuenta con ([^\n]*?empleados)[^\n]*?facturación anual de ([^\n]+?)\.',t)
    if m: o['ie_emp'],o['ie_rev']=m.group(1),m.group(2)
    m=re.search(r'(?i)fecha de constituci[oó]n[^\n]*\n?\s*(\d\d/\d\d/\d{4})',t) or re.search(r'(?i)constituida? (?:el|en) (?:el )?(\d\d/\d\d/\d{4})',t)
    o['const']=m.group(1) if m else ''
    return o
# query-key variant used for the cached infoempresa suggestion lookups (kept for cache compatibility; over-strips trailing 'sa'/'sl' letters)
LEGAL_OLD=r'(?i)[,\s]*(S\.?\s?L\.?\s?L\.?|S\.?\s?L\.?\s?U\.?|S\.?\s?L\.?\s?P\.?|S\.?\s?L\.?|S\.?\s?A\.?\s?L\.?|S\.?\s?A\.?\s?U\.?|S\.?\s?A\.?|S\.?\s?Coop\.?( Pequeña)?|Sdad\.? Coop\.?|KOOP\.? ELK\.?( TXIKIA)?|S COOP( PEQUEÑA)?|A\.?I\.?E\.?|SOCIEDAD LIMITADA)\s*$'
def qkey(n):
    n=re.sub(r'\s*\(.*?\)\s*$','',n.strip())
    for _ in range(2): n=re.sub(LEGAL_OLD,'',n).strip(' ,.')
    return n
