import sys
from datetime import datetime

daily_sales = [0] * 7
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        date, sales = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        daily_sales[weekday] += float(sales)

for weekday, total_sales in enumerate(daily_sales):
    print("{0}\t{1}".format(weekday, total_sales))