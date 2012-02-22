import numpy as np
import matplotlib.pyplot as plt
import pandas

import parsetmy
import getwunderground


r1 = parsetmy.load()
r2 = getwunderground.load()

fig = plt.figure()
ax1 = fig.add_subplot(111)

#ax1.plot(r1.date_mmddyyyy, r1.dewpoint_c, 'o-')
ax1.plot(r1.date_mmddyyyy, pandas.stats.moments.ewma(r1.dewpoint_c,span=24*14), 'o-')
ax1.plot(r2['datetime'], r2['dewptm']-pandas.stats.moments.ewma(r1.dewpoint_c,span=24*14), 'o-')

#ax2 = fig.add_subplot(212)
#ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
