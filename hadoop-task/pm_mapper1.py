#!/usr/bin/env python
import sys

for line in sys.stdin:
    event_id, case_id, activity, timestamp = line.strip().split('\t')[0:4]
    print("{}-{}\t{}".format(case_id, timestamp, activity))