
import json
import csv
from collections import Counter


def json_parser(filename):
    f = open(filename, 'r')
    raw = json.load(f)
    text = raw['text']
    words = text.split(" ")
    wc = Counter(words)
    num = len(words)
    f.close()
    return {'wordcount': wc, 'numwords': num}

def csv_parser(filename, col_name):
    content_lst = []  # an empty list to store the second column
    cnt
    with open(filename, 'r') as rf:
        reader = csv.reader(rf, delimiter=',')
        for row in reader:
            content_lst.append(row[1])

        for word in content_lst:
            Counter([word]) += 1

    return {'wordcount': wc, 'numwords': num}