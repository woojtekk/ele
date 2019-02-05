#!/bin/bash
rr=\""$HOME/inhouse/2018/run07_18_xrd_mainz/ele/raw.txt"\"
ff=\""$HOME/inhouse/2018/run07_18_xrd_mainz/ele/data/"$1".raw"\"

echo $rr
echo $ff
gnuplot -persist <<-EOFMarker
reset
set term x11
set grid
set y2tics
set xlabel "time [s]"

plot $rr u 1:3 w l lt 1 lw 2 axes x1y1 t "raw  column 1" ,"" u 1:2 w l lt 2 lw 2 axes x1y2 t "raw  column 2", $ff u 1:3 w l lt 3 lw 2 axes x1y1 t "file column 1" ,"" u 1:2 w l lt 4 lw 2 axes x1y2 t "file column 2"

pause -1

EOFMarker
