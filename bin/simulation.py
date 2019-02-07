#!/usr/bin/python
# -*- coding: utf-8 -*-
import K2400
import random
import time
import K2400_plot
x=0

pl=K2400_plot.plot()

while True:
    txt = str(x) + " " + str(random.randint(0,10)) + " \t" + str(random.random()*100)+"\n"
    print txt
    pl.plt_update(txt)

    with open(K2400.PATH+"/data/test.txt", 'a') as file:  file.write(txt)

    x += 1
    time.sleep(0.5)

    if x>=2000 : break