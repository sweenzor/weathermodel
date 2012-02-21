#!/usr/bin/env python

import requests
import json
import datetime
from numpy import array, zeros

def jsondate(date_dict):

    yr = int(date_dict['year'])
    mn = int(date_dict['mon'])
    dy = int(date_dict['mday'])
    hr = int(date_dict['hour'])

    return datetime.datetime(yr,mn,dy,hr)


api_key = 'fae7d20f3531b884'
date = '20101018'
url = 'http://api.wunderground.com/api/%s/history_%s/q/SFO.json' % (api_key, date)
r = requests.get(url)

entry = json.loads(r.content)

x = zeros(25, dtype=[('datetime', '|O8'), ('dewptm', '<f8')])

for index, day in enumerate(entry['history']['observations']):
    x[index] = (jsondate(day['date']), float(day['dewptm']))

print x
