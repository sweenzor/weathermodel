import numpy as np
import matplotlib.pyplot as plt
import pandas.stats.moments as moments

import parsetmy
import getwunderground


typical = parsetmy.load()
current = getwunderground.load()

fig = plt.figure()
ax1 = fig.add_subplot(111)

#ax1.plot(r1.date_mmddyyyy, r1.dewpoint_c, 'o-')
ax1.plot(typical.date_mmddyyyy, moments.ewma(typical.dewpoint_c,span=24*14), 'o-')
ax1.plot(current['datetime'], moments.ewma(current['dewptm'],span=24), 'o-')

#ax2 = fig.add_subplot(212)
#ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
