import pandas as pd
from typing import List
from collections import Counter, defaultdict
import random
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pprint as pp

nltk.download('stopwords')
nltk.download('wordnet')

def _default_parser(filename):
    """
    We'll use this method to do the parsing steps for txt files
    :param filename:
    :return:
    """
    # read in txt file into string
    with open(filename) as f:
        content = f.read()

    # pre-process the content
    content = SentimentNLP.preprocess(content)

    # this results dict will have the statistics and stuff for each file, no need to save the actual string
    # We need wordcount,
    results = {
        'wordcount': Counter("to be or not to be".split()),
        'numwords': random.randrange(10, 50)
    }
    return results

def preprocess(content):
 # this takes out puncuation, lower cases everything, combined similar words, takes out stop words/ non-words.
    text_data = content
    text_data = re.sub('[^a-zA-Z]', ' ', text_data)
    text_data = text_data.lower()
    text_data = text_data.split()
    wl = WordNetLemmatizer()
    text_data = [wl.lemmatize(word) for word in text_data if not word in set(stopwords.words('english'))]
    text_data = ' '.join(text_data)

    return text_data


def count(text):
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def main():
    with open('49924_0.txt') as f:
        content = f.read()
        content = preprocess(content)

    counting_dict = count(content)

    pp.pprint(counting_dict)

    top_five = sorted(counting_dict.values(), reverse=True)[:5]

    print(top_five)
    top_five_dict = {k: v for k, v in counting_dict.items() if v in top_five}
    print(top_five_dict)

main()
