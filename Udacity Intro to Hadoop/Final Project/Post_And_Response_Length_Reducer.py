import sys

count = 0
total = 0
prev_question_id = None
prev_body = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 3:
        question_id, body, answer = data
        if prev_question_id is not None and question_id != prev_question_id:
            print('{0}\t{1}\t{2}'.format(prev_question_id, prev_body, total / float(count)))
            count = 0
            total = 0
        prev_question_id = question_id
        prev_body = body
        count = count + 1
        total += int(answer)

if prev_question_id is not None:
    print('{0}\t{1}\t{2}'.format(prev_question_id, prev_body, total / float(count)))
