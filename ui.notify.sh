#!/bin/sh

UI_COFFEE="./ui.coffee"

while true; do
    inotifywait "$UI_COFFEE"
    sleep 0.3
    "$UI_COFFEE" >tmp/ui.json
done
