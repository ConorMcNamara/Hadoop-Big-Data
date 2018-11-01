import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    author_id = line[3]
    # Time is inputted as "2012-02-25 08:11:01.623548+00"
    hour = int(line[8][11:13])
    print('{0}\t{1}'.format(author_id, hour))
