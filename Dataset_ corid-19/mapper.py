import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 5:
        Date, Country, Confirmed, Deaths, Recovered = data
        print ("{0},{1},{2}".format(Country, Confirmed, Deaths))
