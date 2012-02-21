import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook

import os
import datetime

datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
print 'loading', datafile
r1 = mlab.csv2rec(datafile)

datafile = os.getcwd()+'/724940TY.csv'
print 'loading', datafile
r2 = mlab.csv2rec(datafile, skiprows=1)


# combine date and time columns
for r in r2:
    raw_time = r[1].split(':')
    raw_time = [int(t) for t in raw_time]
    if raw_time[0] == 24:
        raw_time[0] = 0

    time = datetime.time(raw_time[0],raw_time[1])
    datetime.datetime.combine(r[0], time)


r1.sort()
r1 = r1[-300:]

#print r1.dtype.names

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(r1.date, r1.open, 'o-')

ax2 = fig.add_subplot(212)
ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
