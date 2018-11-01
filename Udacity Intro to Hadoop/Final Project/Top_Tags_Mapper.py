import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if(len(line)) == 19:
        tag_id = line[0]
        tag_names = line[2]
        node_type = line[5]
        if node_type == 'question':
            tags = tag_names.lower().split(' ')
            for tag in tags:
                writer.writerow([tag, tag_id])