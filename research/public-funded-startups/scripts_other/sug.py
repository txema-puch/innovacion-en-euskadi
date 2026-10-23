import json,sys,os,re,time,urllib.request,urllib.parse,hashlib
W=sys.argv[1]; recs=json.load(open(W+'/recs.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def strip_legal(n): return re.sub(r'(?i)[,\s]*(S\.?\s?L\.?\s?L\.?|S\.?\s?L\.?\s?U\.?|S\.?\s?L\.?|S\.?\s?A\.?\s?L\.?|S\.?\s?A\.?\s?U\.?|S\.?\s?A\.?|S\.?\s?Coop\.?( Pequeña)?|Sdad\.? Coop\.?|KOOP ELK TXIKIA|S COOP PEQUEÑA|A\.?I\.?E\.?)\s*$','',n).strip(' ,.')
qs=set()
for r in recs:
    qs.add(r['cif'] if r['cif'] else strip_legal(r['name']))
for q in sorted(qs):
    fn=W+'/dl/sug/'+hashlib.md5(q.encode()).hexdigest()+'.json'
    if os.path.exists(fn) and os.path.getsize(fn)>20: continue
    u='https://www.infoempresa.com/sugerencias?q='+urllib.parse.quote(q)
    for i in range(3):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA,'Accept':'application/json'}),timeout=30).read()
            open(fn,'wb').write(json.dumps({'q':q,'resp':json.loads(d)}).encode()); break
        except Exception as e:
            print('ERR',q,e,flush=True); time.sleep(5)
    time.sleep(0.8)
print('done',len(qs))
