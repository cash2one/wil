#!/bin/sh
render() {
    echo "package assets { public final class _$1 {"
    for f in $(ls); do
        echo "[Embed(source='../../data/$1/$f', mimeType='application/octet-stream')] public static const _$f:Class;"
    done
    echo "}}"
}

for i in $(ls); do
    if [ -d $i ]; then
        cd $i
        render $i >../_$i.as
        cd -
    fi
done

exit



TXT="files.txt"
: >$TXT
for i in $(ls); do
    find $i | sort -n -t / -k 2 >>$TXT
done
