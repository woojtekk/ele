#!/bin/bash

fname=$1".png"
echo "image file name: " $fname

gnuplot -persist <<-EOFMarker
    reset
    set grid
    set title "$1"
    plot for[x=4:40:4] "$1" u 1:x w l lw 4
    set terminal png
    set output "$fname"
    replot
EOFMarker

