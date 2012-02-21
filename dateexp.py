import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook

import datetime
import parsetmy

datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
print 'loading', datafile
r1 = mlab.csv2rec(datafile)

r2 = parsetmy.load()
r2 = r2[:240]
print r2.dtype

print list(r2.date_mmddyyyy).index(datetime.datetime(2004, 1, 10, 17, 0))

r1.sort()

#print r1.dtype.names

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(r1.date, r1.open, 'o-')

ax2 = fig.add_subplot(212)
ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
