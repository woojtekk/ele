#!/bin/bash
plik=`pwd`
plik2=$(dirname $plik)"/wd/change.txt"

echo "VDS="$1 > $plik2
