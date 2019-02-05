#!/bin/bash

for i in `seq 1 $1`;
do
name=$2"_biasstres_"$i
echo $name
./K2400.py -c -50 -50 -f $name&
sleep 300
stop.sh
sleep 1
./K2400.py -t 50 0 50 1 -f $name
done 

