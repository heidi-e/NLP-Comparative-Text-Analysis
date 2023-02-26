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

# change
"""
class Textastic:

    def __init__(self):
        # manage data about the different texts that
        # we register with the framework
        self.data = defaultdict(dict) # our data extracted from text files
        self.viz = {}                 # name -> visualization function

    @staticmethod
    def _default_parser(filename):
        results = {
            'wordcount': Counter("to be or not to be".split()),
            'numwords': random.randrange(10, 50)
        }
        return results

    def _save_results(self, label, results):
         Integrate parsing results into internal state
        label: unique label for a text file that we parsed
        results: the data extracted from the file as a dictionary attribute-->raw data
        
        for k, v in results.items():
            self.data[k][label] = v

    def load_text(self, filename, label=None, parser=None):
        Register a document with the framework 
        if parser is None:  # do default parsing of standard .txt file
            results = Textastic._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        # Save / integrate the data we extracted from the file
        # into the internal state of the framework

        self._save_results(label, results)

    def load_visualization(self, name, vizfunc, *args, **kwargs):
        self.viz[name] = (vizfunc, args, kwargs)

    def visualize(self, name=None):
        if name is None: # run all
            for _, v in self.viz.items():
                vizfunc, args, kwargs = v
                vizfunc(self.data, *args, **kwargs)
        else: # run only the named visualization
            vizfunc, args, kwargs = self.viz[name]
            vizfunc(self.data, *args, **kwargs)

"""


class SentimentNLP:
    """
    class for analyzing text using natural language processing
    """

    def __init__(self):
        # manage data about the different texts that
        # we register with the framework
        self.data = defaultdict(dict)


    def _default_parser(self, filename):
        """
        We'll use this method to do the parsing steps for txt files
        :param filename:
        :return:
        """
        # read in txt file into string
        with open(filename) as f:
            content = f.read()

        # pre-process the content
        content = self.preprocess(content)

        # this results dict will have the statistics and stuff for each file, no need to save the actual string
        # We need wordcount,
        top_five = SentimentNLP.count(content)

        results = {
            'wordcount': top_five,
            'otherstats': 20,
        }
        return results

    def count(content):
        """
        takes in a parsed/cleaned string from txt file
        return: dictionary with key as word and value as word counts
        """
        counts = dict()
        words = content.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1


        top_five_values = sorted(counts.values(), reverse=True)[:5]
        print(top_five_values)
        top_five_dict = {k: v for k, v in counts.items() if v in top_five_values}
        return top_five_dict



    def _save_results(self, label, results):
        """ Integrate parsing results into internal state
        label: unique label for a text file that we parsed
        results: the data extracted from the file as a dictionary attribute-->raw data
        """
        for k, v in results.items():
            self.data[k][label] = v


    def load_text(self, filename, label=None, parser=None):
        """ Register a document with the framework """

        if parser is None:  # do default parsing of standard .txt file
            results = self._default_parser(filename)

        else:
            results = parser(filename)

        # also do the processing steps before saving the file
        if label is None:
            label = filename

        # Save / integrate the data we extracted from the file
        # into the internal state of the framework

        self._save_results(label, results)

        #pp.pprint(self._save_results())

    def load_stop_words(self, stopfile):
        """

        :param stopfile:
        :return:
        """
        pass

    def wordcount_sankey(self, word_list: List = None, k: int = 5):
        """

        :param word_list:
        :param k:
        :return:
        """
        pass

    def preprocess(self, content):
        """

        :param content: string, the contents of the file
        :return:
        """
        # this takes out puncuation, lower cases everything, combined similar words, takes out stop words/ non-words.
        text_data = content
        text_data = re.sub('[^a-zA-Z]', ' ', text_data)
        text_data = text_data.lower()
        text_data = text_data.split()
        wl = WordNetLemmatizer()
        text_data = [wl.lemmatize(word) for word in text_data if not word in set(stopwords.words('english'))]
        text_data = ' '.join(text_data)

        return text_data

    def second_viz(self):
        pass

    def third_viz(self):
        pass

    def clean_data(self):
        pass




