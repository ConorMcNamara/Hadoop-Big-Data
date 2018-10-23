#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import csv
import sys

writer = csv.writer(sys.stdout, delimiter='\t')

users_attrs = dict()
posts_attrs = dict()

for line in sys.stdin:
    data = line.strip().split('\t')

    # if it's from forum_user
    if data[1] == 'A':
        key_A = data[0]
        data_A = data[2:]

    # if it's from forum_node
    elif data[1] == 'B':
        key_B = data[0]
        data_B = data[2:]

    if key_A == key_B:
        writer.writerow(data_B[:3] + [key_A] + data_B[3:] + data_A)

