#!/bin/bash
# usage: bopv_sum.sh YEAR NUM OUTDIR  -> finds month folder for issue NUM, saves summary xml
Y=$1; N=$2; O=$3; yy=${Y:2:2}; n=$(printf %04d $N)
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
f=$O/s${yy}_${n}.xml; [ -s $f ] && exit 0
est=$(( (N-1)/21 + 1 )); [ $est -gt 12 ] && est=12
for d in 0 1 -1 2 -2 3 -3; do m=$((est+d)); [ $m -lt 1 -o $m -gt 12 ] && continue; mm=$(printf %02d $m)
 c=$(curl -s -A "$UA" -m 20 -o $f.tmp -w '%{http_code}' https://www.euskadi.eus/bopv2/datos/$Y/$mm/s${yy}_${n}.xml)
 if [ "$c" = 200 ]; then echo "$mm" > $f.month; mv $f.tmp $f; exit 0; fi
done; rm -f $f.tmp; echo "MISS $Y $N" </dev/null
