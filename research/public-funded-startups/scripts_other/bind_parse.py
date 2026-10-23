import re,sys,html,json,glob,os
out=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.html')):
    ed=os.path.basename(f)[0]
    t=open(f,'rb').read().decode('utf-8','ignore')
    for m in re.finditer(r'href="(?:https?://web\.archive\.org/web/\d+/)?(https?://bind40\.com/company/[^"/]+/)"[^>]*>([^<]+)</a>(.*?)(?=href="(?:https?://web\.archive\.org/web/\d+/)?https?://bind40\.com/company/|\Z)',t,re.S):
        url,name,rest=m.group(1),html.unescape(m.group(2)).strip(),m.group(3)
        txt=html.unescape(re.sub(r'<[^>]+>',' ',rest)); txt=re.sub(r'\s+',' ',txt)[:600]
        b=re.search(r'is based in ([^.\[]+)',txt)
        out.append(dict(edition=int(ed),name=name,url=url,based=(b.group(1).strip() if b else ''),snip=txt[:300]))
seen={}
for o in out: seen.setdefault((o['edition'],o['name']),o)
out=list(seen.values())
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
import collections
print(collections.Counter(o['edition'] for o in out))
for o in out:
    if re.search(r'(?i)basque|euskadi|bilbao|donostia|san sebasti|vitoria|bizkaia|gipuzkoa|araba|álava|alava|spain',o['based']+o['snip']): print(o['edition'],'|',o['name'],'|',o['based'][:60])
