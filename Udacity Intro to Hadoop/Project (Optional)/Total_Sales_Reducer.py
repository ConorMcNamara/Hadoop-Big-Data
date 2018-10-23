import sys

total_sales = 0
number_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 1:
        sales = data
        total_sales += sales
        number_sales += 1

print('Total\t{}'.format(total_sales))
print("Count\t{}".format(number_sales))