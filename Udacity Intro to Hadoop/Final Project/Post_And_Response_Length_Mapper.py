import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
question_dict = {}
answer_dict = {}

for line in reader:
    if len(line) == 19:
        node_id = line[0]
        body = line[4]
        len_body = len(body)
        node_type = line[5]
        question_id = str(line[7])

        if node_type == "question":
            question_dict[node_id] = len_body
        if node_type == 'answer':
            if question_id not in answer_dict:
                answer_dict[question_id] = [len_body]
            else:
                answer_dict[question_id].append(len_body)

for reader_id in question_dict:
    if reader_id not in answer_dict:
        print("{0}\t{1}\t{2}".format(int(reader_id), int(question_dict[reader_id]), "0"))
    else:
        for length in answer_dict[reader_id]:
            print("{0}\t{1}\t{2}".format(int(reader_id), int(question_dict[reader_id]), length))
