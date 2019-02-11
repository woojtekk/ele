#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging
import K2400


def help():
    logging.basicConfig(filename=K2400.PATH_LOG + '/K2400.log', format='%(asctime)s :: %(name)s :: %(message)s',
                        level=logging.DEBUG)
    logging.info('let it start')

    parser = argparse.ArgumentParser(description='~~~~~~~~~~~~~~~~~ ELECTRIZED GIWAXS ~~~~~~~~~~~~~~~~')

    parser.add_argument('-t',
                        dest='trans',
                        action='append',
                        nargs=4,
                        metavar=('VDS', 'VGS_START', 'VGS_STOP', 'VGS_DELTA '),
                        help='help: TRANSFER test')

    parser.add_argument('-o',
                        dest="out",
                        action='append',
                        nargs=6,
                        metavar=('VDS_START', 'VDS_STOP', 'VDS_DELAT', 'VGS_START', 'VGS_STOP', 'VGS_DELTA '),
                        help='help: OUTPUT test')

    parser.add_argument('-c',
                        dest="timee",
                        action='append',
                        nargs=2, metavar=('VDS', 'VGS'),
                        help='help: TIME measurements test')

    parser.add_argument('-f',
                        dest="filename",
                        help='Output file name',
                        default="tr00")

    parser.add_argument('-s',
                        dest="shutter",
                        type=int,
                        help='CLOSE:  0 [OFF] OPEN 1 [ON]',
                        default=0)

    parser.add_argument('--NPLC',
                        type=float,
                        help='help: NPLC [1]  Fast: 0.1 Normal 1 Slow: 10',
                        default=1.0)

    parser.add_argument('--DEL',
                        type=int,
                        help='help: DEL  [0s] - wait before measurements [seconds]',
                        default=0)

    parser.add_argument('--DCOMP',
                        type=float,
                        help='help: VDS Comp',
                        default=0.001)

    parser.add_argument('--GCOMP',
                        type=float,
                        help='help: VGS Comp',
                        default=0.001)

    parser.add_argument('--wait',
                        dest="wait",
                        type=int,
                        help='help:  mesure current for each point for n sec.',
                        default=0)

    parser.add_argument('--nosweep',
                        help='help: set NO SWEEP measurements',
                        dest="sweep",
                        action="store_false")

    parser.add_argument('-q',
                        help='help: wait  for start command',
                        dest="waitstart",
                        action="store_true")

    parser.add_argument('--fig',
                        help='show real time figure with data',
                        dest="fig",
                        action="store_true")

    parser.add_argument('--test',
                        help='only for simulation',
                        dest="test",
                        action="store_true")


    return parser.parse_args()
