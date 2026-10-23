import csv,re,sys
rows=list(csv.DictReader(open(sys.argv[1])))
for r in rows:
  if r["status"] in ("active","acquired"):
    m=re.search(r"BORME acts (\S*)\.\.(\S*);",r["notes"]); last=m.group(2) if m else ""
    m2=re.search(r"nominal capital ([\d\.,]+)",r["notes"]); cap=m2.group(1) if m2 else ""
    n=re.search(r"(\d+) capital increase",r["notes"]); n=n.group(1) if n else "?"
    web="website live" in r["notes"]; nm=r["name"][:38]
    print(f"{nm:38} last={last:10} incr={n} cap={cap:14} web={web}")
