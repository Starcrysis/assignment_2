#!/usr/bin/env python
import sys
import json

last_case = None
trace = []

for line in sys.stdin:
    case_id__timestamp, activity = line.strip().split('\t')
    case_id = case_id__timestamp.strip().split('-')[0]
    if last_case == case_id:
        trace.append(activity)
    else:
        if last_case:
            print("{}\t{}".format(last_case, json.dumps(trace)))
        last_case = case_id
        trace = [activity]
#Print last trace
if(last_case):
    print("{}\t{}".format(last_case, json.dumps(trace)))
