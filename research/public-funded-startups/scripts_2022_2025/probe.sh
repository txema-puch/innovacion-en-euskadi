#!/bin/bash
# usage: probe.sh outdir id domain
out=$1; id=$2; d=$3
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
fn="$out/${id}__${d}.html"
r=$(curl -sL -m 12 --max-filesize 3000000 -A "$UA" -o "$fn" -w '%{http_code} %{url_effective}' "https://$d/" 2>/dev/null)
code=${r%% *}
if [ "$code" != "200" ]; then r=$(curl -sL -m 10 --max-filesize 3000000 -A "$UA" -o "$fn" -w '%{http_code} %{url_effective}' "http://www.$d/" 2>/dev/null); code=${r%% *}; fi
if [ "$code" = "200" ]; then echo "$id $d $r"; else rm -f "$fn"; fi
