"""
When plotting time series, eg financial time series, one often wants
to leave out days on which there is no data, eh weekends.  The example
below shows how to use an 'index formatter' to achieve the desired plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook

#datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
datafile = '/Users/matt/Development/weathermodel/724940TY.csv'
print 'loading', datafile
r = mlab.csv2rec(datafile, skiprows=1)

r.sort()
r = r[-300:]

print r.dtype.names

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(r.date_mmddyyyy, r.dewpoint_c, 'o-')
#ax.plot(r.date, r.open, 'o-')
fig.autofmt_xdate()


plt.show()