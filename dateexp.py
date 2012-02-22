import numpy as np
import matplotlib.pyplot as plt
import pandas

import parsetmy
import getwunderground


r1 = parsetmy.load()
r2 = getwunderground.load()

fig = plt.figure()
ax1 = fig.add_subplot(111)

del_rows = []
for index, row in enumerate(r2[:-1]):
    if row[0].hour == r2[index+1][0].hour:
        del_rows.append(index)
print len(del_rows)

new = []
for index, row in enumerate(r2):
    if index not in del_rows:
    	new.append(row)


types = [('datetime', '|O8'),
        ('dewptm', '<f8'),
        ('hum', '<f8'),
        ('precipm', '<f8'),
        ('pressurem', '<f8'),
        ('rain', '<f8'),
        ('tempm', '<f8'),
        ('vism', '<f8'),
        ('wgustm', '<f8'),
        ('wspdm', '<f8')]



from numpy import zeros

x = zeros(len(new), dtype=types)

for index, row in enumerate(new):

    x[index] = tuple(row)



import matplotlib.mlab as mlab

filename = '20111231+365.csv'
mlab.rec2csv(x, filename)


quit()


#ax1.plot(r1.date_mmddyyyy, r1.dewpoint_c, 'o-')
ax1.plot(r1.date_mmddyyyy, pandas.stats.moments.ewma(r1.dewpoint_c,span=24*14), 'o-')
ax1.plot(r2['datetime'], r2['dewptm']-pandas.stats.moments.ewma(r1.dewpoint_c,span=24*14), 'o-')

#ax2 = fig.add_subplot(212)
#ax2.plot(r2.date_mmddyyyy, r2.dewpoint_c, 'o-')

fig.autofmt_xdate()
plt.show()
