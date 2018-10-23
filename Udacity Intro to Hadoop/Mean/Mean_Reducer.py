import sys
from datetime import datetime
import collections


def reducer():
    weekday_cost = collections.defaultdict(list)
    for line in sys.stdin:
        date_and_cost = line.strip().split("/t")
        if len(date_and_cost) == 2:
            date, cost = date_and_cost
            weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
            weekday_cost[weekday].append(float(cost))

    for weekday in weekday_cost:
        mean = sum(weekday_cost[weekday]) / len(weekday_cost[weekday])
        print("{0}\t{1}".format(weekday, mean))