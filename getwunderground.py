#!/usr/bin/env python

import requests
import json
import datetime
import time
import os
from numpy import array, zeros, concatenate
from matplotlib import mlab


def jsondate(date_dict):
    """transform json date into datetime"""

    yr = int(date_dict['year'])
    mn = int(date_dict['mon'])
    dy = int(date_dict['mday'])
    hr = int(date_dict['hour'])
    mi = int(date_dict['min'])

    return datetime.datetime(yr,mn,dy,hr,mi)

def fetchday(date):
    "Get observations for one day, put into record"

    # fetch that thang
    api_key = 'fae7d20f3531b884'
    url = 'http://api.wunderground.com/api/%s/history_%s/q/SFO.json' % (api_key, date)
    r = requests.get(url)
    entry = json.loads(r.content)
    print 'fetched ', date

    # rate limit
    print 'sleeping..'
    time.sleep(10)

    # find out how many observations occured (not always 24)
    num_of_entries = len(entry['history']['observations'])

    types = [('datetime', '|O8'),
            ('dewptm', '<f8'),
            ('hum', '<f8'),
            ('precipm', '<f8'),
            ('pressurem', '<f8'),
            ('rain', '<f8'),
            ('tempm', '<f8'),
            ('vism', '<f8'),
            ('wgustm', '<f8'),
            ('wspdm', '<f8')]

    x = zeros(num_of_entries, dtype=types)

    for index, day in enumerate(entry['history']['observations']):

        # eww, use the types 'keys' to load the rows
        row = [jsondate(day['date'])]
        row += [float(day[key[0]]) for key in types[1:]]
        x[index] = tuple(row)

    return x

def getrange(date, num):

    daily_arrays = []

    for day in range(num):

        string_date = date.strftime('%Y%m%d')
        daily_arrays.append(fetchday(string_date))
        date += datetime.timedelta(1)

    full_range = concatenate(daily_arrays, axis=1)
    
    filename = string_date+'+'+str(num)+'.csv'
    mlab.rec2csv(full_range, filename)
    print 'saved as ', filename

    return full_range

def load():

    datafile = os.getcwd()+'/20111231+365.csv'
    print 'loading', datafile
    record = mlab.csv2rec(datafile)

    return record
