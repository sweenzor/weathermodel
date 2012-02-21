#!/usr/bin/env python

fid = open('724940TY.csv', 'r')

print fid.readline()
print fid.readline()

data = []
for line in fid.readlines():
    data.append(line.split(','))

print len(data)
print data[1:4]

fid.close()
