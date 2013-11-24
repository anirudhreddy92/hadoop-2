#!/usr/bin/env python

# Mapper.py
# Part of Mapreduce code for web server log analysis
#
# Extract IP address and file path from the common log format
# %h %l %u %t \"%r\" %>s %b
#
# Written by Hoonio <developer@hoonio.com> on 2013-11-20
# More Python code reference available at wiki.hoonio.com/lab/python

import sys, re

for line in sys.stdin:
    #data = line.strip().split("\t")
    ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
	 filename = re.search('(\"(\S+) (.*?) (\S+)\")', line)
    if ip and filename:
        print "{0}\t{1}".format(ip.group(0), filename.group(3))



#!/usr/bin/python

# Reducer.py
# Part of Mapreduce code for web server log analysis
#
# Compute quantitative analysis on IP address and file path pair data
# %h %l %u %t \"%r\" %>s %b
#
# Written by Hoonio <developer@hoonio.com> on 2013-11-20
# More Python code reference available at wiki.hoonio.com/lab/python

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    print data_mapped
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += 1

if oldKey != None:
    print oldKey, "\t", salesTotal

