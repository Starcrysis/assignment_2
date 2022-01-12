#!/usr/bin/env python
import sys
import json

last_dfr = None
count = 0

for line in sys.stdin:
    dfr, freq = line.strip().split('\t')
    freq = int(freq)
    if last_dfr == dfr:
        count+=freq
    else:
        if last_dfr:
            print("{}\t{}".format(last_dfr, count))
        last_dfr = dfr
        count = freq
#Print last trace
if(last_dfr):
    print("{}\t{}".format(last_dfr, count))