#!/usr/bin/env python
import sys
import json

for line in sys.stdin:
    case_id, trace = line.strip().split('\t')
    trace = json.loads(trace)
    for i in range(len(trace)-1):
        print("{}->{}\t1".format(trace[i], trace[i+1]))