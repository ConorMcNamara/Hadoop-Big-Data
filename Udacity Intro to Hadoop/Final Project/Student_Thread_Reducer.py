import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

prevThread = None
currentThread = None
authors = []

for line in reader:
    if len(line) == 2:
        currentThread, author = line

    if prevThread is not None and prevThread != currentThread:
        writer.writerow([prevThread, ','.join(authors)])
        authors = []

        prevThread = currentThread
        authors.append(author)

if prevThread is not None:
    writer.writerow([prevThread, ','.join(authors)])
