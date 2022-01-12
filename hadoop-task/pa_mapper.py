#!/usr/bin/env python
import sys

for line in sys.stdin:
    event_id, case_id = line.strip().split('\t')[0:2]
    service_time = line.strip().split('\t')[-1]
    print("{}\t{}".format(case_id, service_time))