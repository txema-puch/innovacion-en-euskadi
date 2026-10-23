import sys,glob,os,csv,io,re,json
import xlrd,openpyxl
d=sys.argv[1]; rows=[]
for f in sorted(glob.glob(d+'/*.bin')):
    hdr=open(f[:-4]+'.hdr',errors='ignore').read()
    m=re.search(r'filename="([^"]+)"',hdr); fn=m.group(1) if m else ''
    if fn.endswith('.csv'):
        if re.search(r'(eu|_e_)',fn) and not re.search(r'es\.csv|_c_',fn): continue
        raw=open(f,'rb').read()
        try: t=raw.decode('utf-8')
        except: t=raw.decode('latin-1')
        rd=list(csv.reader(io.StringIO(t),delimiter=';'))
        h=rd[0]
        for r in rd[1:]:
            rows.append(dict(src=fn,**{h[i]:(r[i] if i<len(r) else '') for i in range(len(h))}))
    elif fn.endswith('.xlsx'):
        wb=openpyxl.load_workbook(io.BytesIO(open(f,"rb").read()),read_only=True)
        for ws in wb.worksheets:
            it=list(ws.iter_rows(values_only=True))
            if not it: continue
            hi=0
            for i,r in enumerate(it[:10]):
                if r and sum(1 for x in r if x)>=4: hi=i;break
            h=[str(x) for x in it[hi]]
            for r in it[hi+1:]: rows.append(dict(src=fn,**{h[i]:('' if r[i] is None else str(r[i])) for i in range(min(len(h),len(r)))}))
    elif fn.endswith('.xls'):
        wb=xlrd.open_workbook(f)
        for ws in wb.sheets():
            if ws.nrows==0: continue
            hi=0
            for i in range(min(10,ws.nrows)):
                if sum(1 for x in ws.row_values(i) if str(x).strip())>=4: hi=i;break
            h=[str(x) for x in ws.row_values(hi)]
            for i in range(hi+1,ws.nrows):
                r=ws.row_values(i); rows.append(dict(src=fn,**{h[j]:str(r[j]) for j in range(min(len(h),len(r)))}))
json.dump(rows,open(sys.argv[2],'w'),ensure_ascii=False)
import collections
print(len(rows)); print(collections.Counter(r['src'] for r in rows))
for fn in sorted(set(r['src'] for r in rows)):
    print(fn, [k for k in next(r for r in rows if r['src']==fn).keys()])
