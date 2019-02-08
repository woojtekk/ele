#!/usr/bin/python
# -*- coding: utf-8 -*-


import pip

def install(package):
    pip.main(['install', package])

def install_all_packages(modules_to_try):
    for module in modules_to_try:
        try:
            print "import:", module
            __import__(module)
        except ImportError as e:
            install(e.name)


if __name__ == '__main__':
    txt={"signal",
         "logging",
         "serial",
         "os",
         "fcntl",
         "sys",
         "shutil",
         "datetime",
         "matplotlib",
         "matplotlib",
         "time",
         "random",
         "Tkinter",
         "numpy",
         "time",
         "multiprocessing",}


    install_all_packages(txt)