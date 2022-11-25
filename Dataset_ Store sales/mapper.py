import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 4:
        Store, Dept, Date, Totalsales = data
        print ("{0},{1}".format(Store, Totalsales))
