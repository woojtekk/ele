#!/bin/bash

for i in `seq 1 $1`;
do 
name=$2"_biasstres_"$i
echo $name
./K2400.py -c -60 -60 & 
sleep 60
$3 $4 $5 $6 -f $name
done 

for i in `seq 1 $1`;
do 
name=$2"_biasstres_"$i
echo $name
./K2400.py -t -60 0 -60 1  
wait 60 
$3 $4 $5 $6 -f $name
done
