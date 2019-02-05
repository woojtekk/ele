#!/bin/bash

for i in `seq 1 $1`;
do
name=$2"_biasstres_"$i
echo $name
./K2400.py -t $3 $4 $5 $6 -f $name
done
