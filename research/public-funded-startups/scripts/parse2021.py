import re,sys,json
rows=[]
for l in open(sys.argv[1],encoding='utf-8'):
    m=re.match(r'^(EK-\d{5}-2021)\s+(.+?)\s{2,}([\d\.]+,\d\d)\s*$',l.rstrip())
    if m: rows.append(dict(exp=m.group(1),name=m.group(2).strip(),amount=float(m.group(3).replace('.','').replace(',','.'))))
legal=re.compile(r'(?i)(S\.\s?Coop\.?|S\.\s?L\.?|S\.L\.L\.|S\.L\.U\.|S\.\s?A\.?|S\.\s?Coop|Aie|Sociedad Limitada)\s*$')
for r in rows: r['entity']=bool(legal.search(r['name']))
json.dump(rows,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(rows),sum(r['entity'] for r in rows),sum(r['amount'] for r in rows))
for r in rows:
    if not r['entity']: print('  person?',r['name'])
