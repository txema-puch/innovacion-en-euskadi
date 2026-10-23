import csv,re,collections,sys,json
R=list(csv.DictReader(open(sys.argv[1]))) if __name__=="__main__" else []
def cohort(r):
    p=r['programme']; startup_prog=re.search(r'DFB|TXEKINTEK|BIC Gipuzkoa|BIND|Seed Capital|GCR|fondos de capital',p)
    if startup_prog: return 'A'
    if 'Gauzatu' in p and '-> YOUNG' in r['notes']: return 'A'
    return 'B'
def ventas(r):
    m=re.search(r'ventas ([\d,\.]+)(M|K)? €',r['notes'])
    if not m: return 0
    v=float(m.group(1).replace(',','.')); return v*(1e6 if m.group(2)=='M' else 1e3 if m.group(2)=='K' else 1)
eb={'1-9 (range)':1,'10-49 (range)':2,'más de 50 (range)':3,'50-249 (range)':3,'más de 249 (range)':4}
if __name__=='__main__':
    A=[r for r in R if cohort(r)=='A']; B=[r for r in R if cohort(r)=='B']
    print('A',len(A),collections.Counter(r['classification'] for r in A)); print('B',len(B),collections.Counter(r['classification'] for r in B))
    print('A status',collections.Counter(r['status'].split(' (')[0] for r in A))
    print('A employees (sampled)',collections.Counter(r['employees'] for r in A if r['employees']!='unknown'))
    act=[r for r in A if r['status']=='active']
    top=sorted(act,key=lambda r:(eb.get(r['employees'],0),ventas(r),int(r['capital_increases']) if r['capital_increases'].isdigit() else 0),reverse=True)
    json.dump([r['cif'] for r in sorted(act,key=lambda r:(ventas(r),int(r['capital_increases']) if r['capital_increases'].isdigit() else 0),reverse=True)[:45]],open('top_cands.json','w'))
    for r in top[:25]: print(r['name'][:40],'|',r['programme'][:50],'|',r['employees'],'|',ventas(r),'|',r['capital_increases'],'|',r['classification'])
