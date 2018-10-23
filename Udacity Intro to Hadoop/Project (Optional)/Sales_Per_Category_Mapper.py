#!/usr/bin/python


# Format of each line is:
# date\t time\t store_name\t item_description\t price\t method_of_payment
#
# We want elements 3 (item name) and 4 (price) to find a sales breakdown
# by product category across all of the stores.

# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, price, payment = data
        print("{0}\t{1}".format(item, price))
