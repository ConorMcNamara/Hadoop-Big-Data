import sys


def mapper():
    for line in sys.stdin:
        purchase_data = line.strip().split("\t")
        if len(purchase_data) == 6:
            date, time, store, item, cost, payment = purchase_data
            print("{}\t{}".format(date, cost))