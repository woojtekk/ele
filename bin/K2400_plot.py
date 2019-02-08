#!/usr/bin/python
# -*- coding: utf-8 -*-
import K2400
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os
import time
import random
from Tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np



class plot():

    def __init__(self):
        self.path = K2400.PATH
        with open(self.path+ "/FName", 'r') as f: self.FName = str(f.readline())
        self.plt_init()

        return None

    def plt_init(self):
        self.pl=plt
        self.pl.ion()
        self.pl.xlabel("VGS [V] or TIME [s]")
        self.pl.ylabel("IDS [A]")
        self.pl.grid(True)
        self.pl.title(os.path.basename(self.path))
        self.pl.axis([-1, 1, -1e-10, 1e-10])
        self.pl.show()


    def plt_update(self,x,y):

        self.pl.scatter(x,y)#, self.txt.split()[2])
        self.pl.autoscale(enable=True, axis="both", tight=True)

        self.pl.pause(0.01)
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

    def plt_file(self,):

        try:
            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename(initialdir = K2400.PATH+"/data/", filetypes = (("txt files","*.txt"),("all files","*.*")))  # show an "Open" dialog box and return the path to the selected file
            x, y = np.loadtxt(filename, delimiter=' ', unpack=True,usecols=[0,1])
        except TypeError:
            quit()

        self.plt_update(x,y)
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass

    def save_png(self):
        f=str(os.path.splitext(self.FName)[0]+".png")
        print "PNG saved to file:", f
        plt.savefig(f)
        return 0

if __name__ == '__main__':
    grf=plot()
    grf.plt_file()


