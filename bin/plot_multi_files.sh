#!/bin/bash
fname=$1|tr "_" "-"
echo $*  | tr " " "\n"| sort --version-sort >list
#ls "$fname" >> lista

fname=$1".png"
echo "Image file name: " $fname

gnuplot -persist <<-EOFMarker
    reset
    set grid
    set title "$1"
    plot for [file in system("cat ./list")] file notitle
    set terminal png
    set output "$fname"
    replot
EOFMarker


rm list
