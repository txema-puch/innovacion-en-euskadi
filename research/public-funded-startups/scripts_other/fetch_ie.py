import json,sys,os,subprocess,time,csv,hashlib,urllib.parse
W=sys.argv[1]; E=json.load(open(W+'/ents.json'))
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
rows={r['cif']:r for r in csv.DictReader(open(W+'/startups_other.csv'))}
# 1) CIF-only entities: retry suggestion lookup
for e in E:
    if e['cif'] and not e['uri']:
        q=e['cif']; fn=W+'/dl/sug/'+hashlib.md5(q.encode()).hexdigest()+'.json'
        r=subprocess.run(['curl','-s','-4','-m','30','-A',UA,'-H','Accept: application/json','https://www.infoempresa.com/sugerencias?q='+q],capture_output=True)
        try: d=json.loads(r.stdout); open(fn,'w').write(json.dumps({'q':q,'resp':d}))
        except Exception: print('blocked at sug',q,flush=True); break
        time.sleep(2.5)
# 2) company pages: systematic sample = all GROWING/ABSORBED + every 3rd other in-CSV entity with infoempresa URI (CSV order)
sample=[];i=0
for e in E:
    r=rows.get(e['cif'])
    if not r or not e['uri']: continue
    if r['classification'] in ('GROWING','ABSORBED') or i%3==0: sample.append(e)
    if r['classification'] not in ('GROWING','ABSORBED'): i+=1
json.dump([e['cif'] for e in sample],open(W+'/ie_sample.json','w'))
print('sample',len(sample),flush=True)
for e in sample:
    fn=W+'/dl/ie/'+e['cif']+'.html'
    if os.path.exists(fn) and os.path.getsize(fn)>20000: continue
    c=subprocess.run(['curl','-sL','-4','-m','30','-A',UA,'-o',fn,'-w','%{http_code}','https://www.infoempresa.com'+e['uri']],capture_output=True,text=True).stdout
    if c=='403': print('blocked',e['cif'],flush=True); time.sleep(120)
    time.sleep(2.5)
print('done',flush=True)
