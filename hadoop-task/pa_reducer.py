#!/usr/bin/env python
import sys

last_case = None
total_servicetime = 0

for line in sys.stdin:
    case_id, duration = line.strip().split('\t')
    duration = float(duration)
    if last_case == case_id:
        total_servicetime += duration
    else:
        if last_case:
            print("{}\t{}".format(last_case, total_servicetime))
        last_case = case_id
        total_servicetime = duration
#Print last trace
if(last_case):
    print("{}\t{}".format(last_case, total_servicetime))
