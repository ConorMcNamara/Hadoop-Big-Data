import sys

highest_sale = 0
prev_store = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        store, sales = data
        sales = float(sales)
        if store != prev_store and prev_store is not None:
            print("{0}\t{1}".format(prev_store, highest_sale))
            highest_sale = 0

        prev_store = store
        if sales > highest_sale:
            highest_sale = sales

# Our loop misses printing out the last store, so we do it ourselves (just also need to make sure the last store
# isn't None)
if prev_store is not None:
    print('{0}\t{1}'.format(prev_store, highest_sale))
