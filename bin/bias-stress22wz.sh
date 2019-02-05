#!/bin/bash

for i in `seq 1 $1`;
do
name=$2"_biasstres_"$i
echo $name
./K2400.py -c -60 -60 -f $name&
sleep 10
stop.sh
sleep 1
./K2400.py -t -60 5 -60 1 -f $name
done 

