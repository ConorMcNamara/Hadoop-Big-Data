import sys

hour_count = [0] * 24
prev_author_id = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        author_id, hour = data
        if prev_author_id is not None and author_id != prev_author_id:
            for hour, count in enumerate(hour_count):
                if count == max(hour_count):
                    print('{0}\t{1}'.format(prev_author_id, hour))
            hour_count = [0] * 24
        prev_author_id = author_id
        hour_count[int(hour)] += 1

# Our for loop neglects to print the last author, so we need to do so on the condition that the last author actually
# exists
if prev_author_id is not None:
    for hour, count in enumerate(hour_count):
        if count == max(hour_count):
            print('{0}\t{1}'.format(prev_author_id, hour))