#!/usr/bin/env python

import matplotlib.mlab as mlab
import os
import datetime


def fixdatetime(record):
    """combine date and time columns"""

    for r in record:
        raw_time = r[1].split(':')
        raw_time = [int(t) for t in raw_time]

        # move from 1..24 to 0..23
        raw_time[0] = raw_time[0]-1

        time = datetime.time(raw_time[0],raw_time[1])
        r[0] = datetime.datetime.combine(r[0], time)


def setyear(yr, record):
    """set year of all data"""
    
    for r in record:
        r[0] = r[0].replace(year=yr)


def load():

    datafile = os.getcwd()+'/724940TY.csv'
    print 'loading', datafile
    record = mlab.csv2rec(datafile, skiprows=1)
    fixdatetime(record)
    setyear(2004,record)

    return record
