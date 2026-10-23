#!/bin/bash
# usage: getwb.sh URL OUTFILE [TIMESTAMP]  -> live first, then Wayback id_ fallback
U=$1; F=$2; TS=${3:-2024}
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
c=$(curl -sL -A "$UA" -m 40 -o "$F" -w '%{http_code}' "$U")
ok(){ [ -s "$F" ] && ! grep -qi 'Temporarily Offline' "$F" 2>/dev/null; }
if [ "$c" = 200 ] && ok; then echo "LIVE $c $U"; exit 0; fi
for i in 1 2 3; do c=$(curl -sL -m 120 -o "$F" -w '%{http_code}' "https://web.archive.org/web/${TS}id_/$U"); if [ "$c" = 200 ] && ok; then echo "WAYBACK $TS $U"; exit 0; fi; sleep 5; done
echo "FAIL $c $U"; exit 1
