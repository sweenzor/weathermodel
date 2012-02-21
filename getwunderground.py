#!/usr/bin/env python

import requests

api_key = 'fae7d20f3531b884'
loc = 'CA/San_Francisco.json'
url = 'http://api.wunderground.com/api/%s/hourly10day/q/%s' % (api_key,loc)

url = 'http://api.wunderground.com/api/%s/history_20101018/q/SFO.json' % api_key

r = requests.get(url)

print r.content
