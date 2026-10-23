import json,sys,os,re,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import base
rows=json.load(open(sys.argv[1]))
STOP={'technologies','technology','tech','solutions','solution','the','company','europe','iberia','data','health','media','systems','system','delivery','innovation','app','labs','lab','grupo','group','global','smart','digital','green','basque','euskadi','bilbao','new','advanced','ingenieria','engineering','consulting','servicios','services','soluciones','industrial','energy','bio','sistemas','studio','spain','international','software','the','de','del','la','el','y','and','for','2021','2022','2023','2024','2025','sport','robotics','game','games','ai','ia','food','design','team','city','life','world','project','projects','home'}
def asc(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
for r in rows:
    b=asc(base(r['name'])); words=re.findall(r'[a-z0-9]+',b)
    c=[''.join(words)]
    if len(words)>1:
        if words[0] not in STOP and len(words[0])>3: c.append(words[0])
        c.append(words[0]+words[1]) if len(words)>2 else None
        c.append('-'.join(words))
    for d in dict.fromkeys(x for x in c if x and len(x)<=40):
        for tld in ['com','es','io','eus','ai','tech']:
            print(r['id'],f'{d}.{tld}')
