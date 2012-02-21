#!/usr/bin/env python

import requests
import json
import datetime
from numpy import array

api_key = 'fae7d20f3531b884'
date = '20101018'
url = 'http://api.wunderground.com/api/%s/history_%s/q/SFO.json' % (api_key, date)
r = requests.get(url)

entry = json.loads(r.content)


x = array([], dtype=[('datetime', '|O8'), ('dewptm', '<i8')])


for day in entry['history']['observations']:
	print day['date']['hour']
	print day['dewptm']


#print json.dumps(entry['history']['observations'], sort_keys=True, indent=4)
