import json,sys,os,re,time,subprocess,urllib.parse,hashlib
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__)); from parsers import strip_legal,qkey
W=sys.argv[1]; recs=json.load(open(W+'/recs.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
qs=sorted(set(r['cif'] if r['cif'] else qkey(r["name"]) for r in recs) | set(sys.argv[2:]))
def get(q):
    fn=W+'/dl/sug/'+hashlib.md5(q.encode()).hexdigest()+'.json'
    if os.path.exists(fn) and os.path.getsize(fn)>20: return
    u='https://www.infoempresa.com/sugerencias?q='+urllib.parse.quote(q)
    for i in range(3):
        r=subprocess.run(['curl','-s','-4','-m','30','-A',UA,'-H','Accept: application/json',u],capture_output=True)
        try: d=json.loads(r.stdout); open(fn,'w').write(json.dumps({'q':q,'resp':d})); return
        except Exception: time.sleep(3)
    print('FAIL',q,flush=True)
with ThreadPoolExecutor(4) as ex: list(ex.map(get,qs))
print('done',len(qs))
