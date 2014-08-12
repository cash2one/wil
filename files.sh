#!/bin/sh
TXT="files.txt"
: >$TXT
for i in $(ls); do
    find $i | sort -n -t / -k 2 >>$TXT
done
