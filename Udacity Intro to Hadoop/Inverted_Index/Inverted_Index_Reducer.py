import sys
import collections

def reducer():

    for line in sys.stdin:
        word_and_id = line.strip().split("\t")
        inverted_index = collections.defaultdict(list)
        if len(word_and_id) != 2:
            continue
        word = word_and_id[1].lower()
        word_id = word_and_id[0]
        inverted_index[word].append(word_id)

    for word in inverted_index:
        print("{0}\t{1}\t{2}".format(word, len(inverted_index[word]), inverted_index[word]))