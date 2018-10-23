import sys

total_sales = 0
prev_category = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        item_category, sales = data
        if item_category != prev_category and prev_category is not None:
            print("{0}\t{1}".format(prev_category, total_sales))
            total_sales = 0

        prev_category = item_category
        total_sales += sales

# Our loop misses printing out the last category, so we do it ourselves (just also need to make sure the last category
# isn't None)
if prev_category is not None:
    print('{0}\t{1}'.format(prev_category, total_sales))
