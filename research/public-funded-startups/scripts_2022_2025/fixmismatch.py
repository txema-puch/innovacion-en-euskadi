import glob,re,os,sys
for f in sorted(glob.glob(sys.argv[1]+'/*_ie.html.*.mismatch')):
    t=open(f,'rb').read().decode('utf-8','ignore'); m=re.search(r'empresaCif:\s*"([A-Z0-9]*)"',t)
    tgt=f.split('.html')[0]+'.html'
    if m and m.group(1)=='' and not os.path.exists(tgt): os.rename(f,tgt); print('accepted (empty CIF)',os.path.basename(tgt))
    elif m: print('real mismatch',os.path.basename(f),m.group(1))
