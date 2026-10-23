import sys,re,html
for f in sys.argv[1:]:
    b=open(f,'rb').read()
    try: t=b.decode('utf-8')
    except: t=b.decode('latin-1')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?i)<(br|/p|/tr|/li|/h\d|/div)[^>]*>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    print(t)
