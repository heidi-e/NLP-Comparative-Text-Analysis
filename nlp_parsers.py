
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

def csv_parser(filename):
    with open(filename, 'w', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for words in row:
                wc = Counter(words)
                num = len(words)
    return {'wordcount': wc, 'numwords': num}