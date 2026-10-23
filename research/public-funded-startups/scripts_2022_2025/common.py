import re,unicodedata,html
SUF=r'(?i)[\s,\.]*(sociedad limitada laboral|sociedad limitada unipersonal|sociedad limitada|sociedad anonima|sociedad anónima|s\.?\s?coop\.?( pequeña)?|sociedad cooperativa|s\s?\.?\s?l\s?\.?\s?[lp]\.?|s\.?\s?a\.?\s?[dl]\.?|s\s?\.?\s?l\s?\.?\s?u\.?|s\s?\.?\s?l\.?|s\s?\.?\s?a\.?\s?u?\.?|s\.c\.|a\.?i\.?e\.?)\s*\.?$'
def base(n):
    b=re.sub(r'\.\.+','.',n.strip())
    for _ in range(2): b=re.sub(SUF,'',b).strip(' ,.')
    return b
def suffix(n):
    t=n.lower().replace(' ','')
    if 'coop' in t: return 'coop'
    if re.search(r'(s\.?l\.?l\.?|limitadalaboral)$',t): return 'sll'
    if re.search(r'(s\.?l\.?u\.?|unipersonal)$',t): return 'slu'
    if re.search(r'(s\.?a\.?u?\.?|anonima|anónima)$',t): return 'sa'
    return 'sl'
def slug(s): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
def txt(fn):
    b=open(fn,'rb').read().decode('utf-8','ignore')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b); b=re.sub(r'<[^>]+>','\n',b); b=html.unescape(b).replace('\xa0',' ')
    return re.sub(r'[ \t]+',' ',re.sub(r'\s*\n\s*','\n',b))
