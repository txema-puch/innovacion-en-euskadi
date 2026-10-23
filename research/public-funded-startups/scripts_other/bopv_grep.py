import re,sys,glob,os
pat=re.compile(sys.argv[2],re.I)
for f in sorted(glob.glob(sys.argv[1]+'/*.xml')):
    t=open(f,'rb').read().decode('utf-8','ignore')
    mo=open(f+'.month').read().strip() if os.path.exists(f+'.month') else '??'
    yy=os.path.basename(f)[1:3]
    for m in re.finditer(r'<BOPVSumarioTitulo>(.*?)</BOPVSumarioTitulo>\s*<BOPVSumarioOrden>(\d+)</BOPVSumarioOrden>',t,re.S):
        if pat.search(m.group(1)):
            print(f"20{yy}/{mo} {os.path.basename(f)} {yy}0{int(m.group(2)):04d}a | {m.group(1)[:400]}")
