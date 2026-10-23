import json,re,unicodedata,subprocess,sys,os,html
rows=json.load(open(sys.argv[1])); out=sys.argv[2]
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def base(n): return re.sub(r'(?i),?\s*(S\.\s?Coop\.?|S\.L\.L\.|S\.L\.U\.|S\.\s?L\.?|S\.\s?A\.?|Aie|Sociedad Limitada)\s*$','',n).strip()
def sl(s): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
stop={'technologies','technology','solutions','solution','sl','the','company','europe','iberia','data','health','media','systems','delivery','innovation','app','labs'}
for r in rows:
    if not (r['entity'] or r['name'] in ('Nutrenaissance','Impulso Cognitivo')): continue
    b=base(r['name']); words=[w for w in re.findall(r'[a-z0-9]+',unicodedata.normalize('NFKD',b).encode('ascii','ignore').decode().lower())]
    cands=[sl(b)]
    if len(words)>1 and words[0] not in stop and len(words[0])>3: cands.append(words[0])
    found=None
    for c in dict.fromkeys(cands):
        for tld in ['com','es','io','eus']:
            u=f"https://{c}.{tld}/"; fn=os.path.join(out,f"{r['exp']}_{c}.{tld}.html")
            p=subprocess.run(['curl','-sL','-m','12','-A',UA,'-o',fn,'-w','%{http_code} %{url_effective}',u],capture_output=True,text=True).stdout
            code=p.split()[0] if p else '000'
            if code=='200' and os.path.getsize(fn)>500:
                t=open(fn,'rb').read().decode('utf-8','ignore')
                m=re.search(r'(?is)<title[^>]*>(.*?)</title>',t); title=html.unescape(m.group(1)).strip()[:80] if m else ''
                key=words[0] if words else c
                hit=key in t.lower()
                print(r['exp'],r['name'],'|',u,'->',p.split()[1] if len(p.split())>1 else '', '|',title,'| brand_in_page=',hit,flush=True)
            else:
                try: os.remove(fn)
                except: pass
