#!/bin/bash
plik=`pwd`
plik2=$(dirname $plik)"/wd/change.txt"

echo "VGS="$1 > $plik2
