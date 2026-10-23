import sys,re,html
pat=re.compile(sys.argv[1],re.I); n=int(sys.argv[2])
for f in sys.argv[3:]:
    t=open(f,'rb').read().decode('utf-8','ignore'); t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    hits=[t[max(0,m.start()-150):m.end()+150] for m in pat.finditer(t)][:n]
    print('==',f.split('/')[-1]); [print('   ',h) for h in hits]
