import json,sys,os,subprocess,time,re,urllib.parse
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(__file__)); from parsers import parse_em,strip_legal,slug
W=sys.argv[1]; E=json.load(open(W+'/ents.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def curl(u,fn):
    for i in range(3):
        r=subprocess.run(['curl','-sL','-4','-m','40','-A',UA,'-o',fn,'-w','%{http_code}',u],capture_output=True,text=True)
        if r.stdout in ('200','404'): return r.stdout
        time.sleep(10)
def ok(s):
    fn=f"{W}/dl/em/{s}.html"
    if not os.path.exists(fn): return False
    o=parse_em(open(fn,errors='ignore').read()); return bool(o and o['status'])
todo=[e for e in E if e['em_slug'] and e['basque'] is not False and not ok(e['em_slug'])]
alias={}
def go(e):
    q=strip_legal(re.sub(r'\s*\(.*\)$','',e['reg_name'] or e['names'][0]))
    fn=f"{W}/dl/emq/{e['em_slug']}.html"
    if not os.path.exists(fn): curl('https://www.empresia.es/busqueda/?q='+urllib.parse.quote(q),fn); time.sleep(0.7)
    t=open(fn,errors='ignore').read()
    links=list(dict.fromkeys(re.findall(r'href="/empresa/([^/"]+)/"',t)))
    s=e['em_slug']; pick=None
    for l in links:
        if l==s or l==s+'-sl' or re.sub(r'-(sl|sa|slu|sll|s-coop)$','',l)==s: pick=l;break
    if not pick:
        c=[l for l in links if l.startswith(s+'-')]
        if len(c)==1: pick=c[0]
    if pick:
        if not os.path.exists(f"{W}/dl/em/{pick}.html"): curl(f'https://www.empresia.es/empresa/{pick}/',f"{W}/dl/em/{pick}.html"); time.sleep(0.7)
        alias[s]=pick
    print(s,'->',pick,flush=True)
with ThreadPoolExecutor(3) as ex: list(ex.map(go,todo))
json.dump(alias,open(W+'/em_alias.json','w'),indent=0)
print('done',len(todo),len(alias))
