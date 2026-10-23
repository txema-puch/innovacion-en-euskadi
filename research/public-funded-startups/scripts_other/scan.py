import sys,re,html
pat=re.compile(r'(?i).{0,90}(©|copyright|ronda de|millones|empleados|profesionales|adquiri|acquired|part of|parte de|Bilbao|Donostia|Gipuzkoa|Bizkaia|Vitoria|Zamudio|Arnett|levantado|raised|inversores|investors).{0,70}')
for f in sys.argv[1:]:
    t=open(f,'rb').read().decode('utf-8','ignore'); t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    hits=[m.group(0) for m in pat.finditer(t)][:5]
    print('==',f.split('/')[-1]); [print('   ',h) for h in hits]
