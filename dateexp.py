import numpy as np
import matplotlib.pyplot as plt

import datetime

import parsetmy
import getwunderground

r1 = parsetmy.load()
r2 = getwunderground.getrange(datetime.datetime(2011,1,1), 365)

fig = plt.figure()


ax1 = fig.add_subplot(111)
ax1.plot(r1.date_mmddyyyy, r1.dewpoint_c, 'o-')
ax1.plot(r2['datetime'], r2['dewptm'], 'o-')

#ax2 = fig.add_subplot(212)
#ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
