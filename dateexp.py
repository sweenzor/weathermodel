"""
When plotting time series, eg financial time series, one often wants
to leave out days on which there is no data, eh weekends.  The example
below shows how to use an 'index formatter' to achieve the desired plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook

datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
print 'loading', datafile
r = mlab.csv2rec(datafile)

r.sort()
r = r[-30:]  # get the last 30 days

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(r.date, r.adj_close, 'o-')
fig.autofmt_xdate()


plt.show()