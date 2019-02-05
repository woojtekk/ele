#!/usr/bin/gnuplot
reset
set term x11
set grid
set y2tics
set xlabel "time [s]"
set ylabel "IGS / A"
set y2label "IDS / A"

plot "/home/saw2user/inhouse/2018/run07_18_xrd_mainz/ele/raw.txt" u 1:3 w l lt 3 axes x1y1 t "IGS" ,"" u 1:2 w l lt 1 lw 3 axes x1y2 t "IDS"

pause -1

