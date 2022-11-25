#!/usr/bin/python
import sys

totalsales = 0
oldId = None


for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue

    thisId, thatsales = data_mapped

    if oldId and oldId != thisId:
        print (oldId, ",", totalsales)
        oldId = thisId;
        totalsales = 0
        

    oldId = thisId
    totalsales += float(thatsales)


if oldId != None:
    print (oldId, ",", totalsales)
