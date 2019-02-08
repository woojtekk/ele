#!/usr/bin/python
# -*- coding: utf-8 -*-
import K2400
import random
import time
import K2400_plot

x=0

pl=K2400_plot.plot()
txt=" buim tarara bum tarara"

while True:

    print txt
    try:
        z = float(txt.split()[0])
        y = float(txt.split()[1])
        pl.plt_update(z, y)
        print z,y
    except ValueError:
        pass

    txt = str(x) + ' ' + str(random.random() / 1000) +' '+ str("asasdas")
    x += 1
    time.sleep(1)

    if x>=2000 : break