#!/usr/bin/python
# -*- coding: utf-8 -*-
import K2400
import matplotlib.pyplot as plt
import os
import time
import random



class plot():

    def __init__(self):
        self.path = K2400.PATH
        with open(self.path+ "/FName", 'r') as f: self.FName = str(f.readline())
        self.plt_init()
        self.plt_update("0 0")
        return None

    def plt_init(self):
        self.pl=plt
        self.pl.xlabel("VGS [V] or TIME [s]")
        self.pl.ylabel("IDS [A]")
        self.pl.grid(True)
        self.pl.title(os.path.basename(self.path))
        self.pl.axis([-1, 1, -1e-10, 1e-10])


    def plt_update(self,txt):

        self.pl.scatter(str(txt.split()[0]), str(txt.split()[1]))#, self.txt.split()[2])
        self.pl.autoscale(enable=True, axis="both", tight=False)
        self.pl.pause(0.05)
        return 0


    def plt_loop(self):
        self.last=""
        while True:
            with open(self.FName.rstrip(), "r") as file:
                try:
                    self.line = (list(file)[-1]).rstrip()

                    if self.line == "": continue
                    if self.line == ">>koniec<<":   break
                    if self.line == self.last:      continue
                    if "#" is self.line:        continue
                    print self.line.split()[0], self.line.split()[1]
                    txt=str(self.line.split()[0])+" "+str(self.line.split()[1])+" "+str(self.line.split()[2])
                    self.plt_update(txt)

                    self.last = self.line
                    time.sleep(0.01)
                except IndexError as error:
                    continue

        return 0

    def save_png(self):
        f=str(os.path.splitext(self.FName)[0]+".png")
        print "PNG saved to file:", f
        plt.savefig(f)
        return 0



if __name__ == '__main__':

    pltt=plot()
    pltt.plt_loop()

    # #x=0
    #
    # while True:
    #     y=random.randint(0,10)
    #     pltt.plt_update(x,y)
    #     print x,y
    #     x+=1
    #     time.sleep(0.1)
    #     if x>=200: break
