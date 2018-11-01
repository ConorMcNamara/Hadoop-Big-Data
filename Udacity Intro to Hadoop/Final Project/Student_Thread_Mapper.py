import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    try:
        if(len(line)) == 19:
            student_id = line[0]
            abs_parent_id = line[7]
            author_id = line[3]
            thread_id = None
            parent_thread_id = abs_parent_id.strip()
            if parent_thread_id is None or parent_thread_id == '\N':
                thread_id = int(student_id)
            else:
                thread_id = int(parent_thread_id)

            writer.writerow([thread_id, author_id])
    except ValueError:
        continue
