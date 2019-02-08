#!/bin/bash

#DIR="/inhouse/2019/run04_19_xrd_mainz/"
DIR="/prog"
HOMEPATH=$HOME$DIR


clear
echo "------------------------------"
echo "-------- Instalacja ----------"
echo "------------------------------"
echo ""

echo "YOUR WORKING DIRECTORY: " $HOMEPATH
echo ""
echo "Downloading ... and extract program .... "
wget -q http://www2.mpip-mainz.mpg.de/~zajaczkowski/elebin.tar.gz
tar -zxf elebin.tar.gz -C $HOMEPATH

echo ""

FF="export PATH=\$PATH:$HOMEPATH/ele/bin"
echo $FF
echo ""

echo $PATH >  ~/.PATH_old.`date "+%s"`

if /bin/grep -Fxq "$FF" $HOME/.bashrc
then
        echo "PATH is already in BASH config file...."
else
        echo "Updating BASH config file .bashrc ..."
    	cp ~/.bashrc  ~/.bashrc.`date "+%s"`
       	echo "$FF" >> ~/.bashrc
fi


if /bin/grep -Fxq "$FF" $HOME/.profile
then
        echo "PATH is already in PROFILE config file...."
else
        echo "Updating PROFILE config file .profile ..."

    	cp ~/.profile ~/.profile.`date "+%s"`

    	echo "$FF" >> ~/.profile
    	$FF
fi


chmod 777 $HOMEPATH/ele/bin/K2400.py
chmod 777 $HOMEPATH/ele/bin/K2400_plot.py
chmod 777 $HOMEPATH/ele/bin/*sh
#
rm elebin.tar.gz*
echo ""
echo "install complete ..."

lp $HOMEPATH/help.pdf

