import sys
import csv

# Mapper
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    specials = ',.!?:;"()<>[]#$=-/'
    trans = str.maketrans(specials, ' ' * len(specials))
    for line in reader:
        if len(line) == 19:
            body = line[4]
            node_id = line[0]
            body = body.translate(trans)
            words = body.strip().split()
            for word in words:
                print("{0}\t{1}".format(word.lower(), node_id))