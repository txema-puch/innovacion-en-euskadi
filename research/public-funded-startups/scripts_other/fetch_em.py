import json,sys,os,subprocess,time
from concurrent.futures import ThreadPoolExecutor
W=sys.argv[1]; E=json.load(open(W+'/ents.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
todo=sorted(set(e['em_slug'] for e in E if e['em_slug'] and e['basque'] is not False))
def get(s):
    fn=f"{W}/dl/em/{s}.html"
    if os.path.exists(fn) and os.path.getsize(fn)>5000: return
    for i in range(3):
        r=subprocess.run(['curl','-sL','-4','-m','40','-A',UA,'-o',fn,'-w','%{http_code}',f'https://www.empresia.es/empresa/{s}/'],capture_output=True,text=True)
        if r.stdout in ('200','404'): break
        time.sleep(10)
    print(s,r.stdout,flush=True); time.sleep(0.7)
with ThreadPoolExecutor(3) as ex: list(ex.map(get,todo))
print('done',len(todo))
