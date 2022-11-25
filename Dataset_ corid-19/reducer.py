#!/usr/bin/python
import sys

totalconfirmed = 0
totaldeaths = 0
oldId = None

for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 3:
        continue

    thisId, mordha, mouta = data_mapped
    

    if oldId and oldId != thisId:
        print (oldId, ",", totalconfirmed,",", totaldeaths)
        oldId = thisId;
        totalconfirmed = 0
        totaldeaths = 0
        

    oldId = thisId
    totalconfirmed += int(mordha)
    totaldeaths+= int(mouta)

if oldId != None:
    print (oldId, ",", totalconfirmed,",",totaldeaths)

