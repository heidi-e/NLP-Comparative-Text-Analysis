import pandas as pd
from typing import List
from collections import Counter, defaultdict
import random
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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
    class for analyzing text stuff
    """

    def __init__(self):
        # manage data about the different texts that
        # we register with the framework
        self.data = defaultdict(dict)

    @staticmethod
    def _default_parser(filename):
        """
        We'll use this method to do the parsing steps
        :param filename:
        :return:
        """
        results = {
            'wordcount': Counter("to be or not to be".split()),
            'numwords': random.randrange(10, 50)
        }
        return results

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

    def preprocess(self, string):
        corpus = []
        text_data = ""
        for i in range(0, 1732(Number of rows)):
            text_data = re.sub('[^a-zA-Z]', ' ', Raw_Data['Column_With_Text'][i])
        text_data = text_data.lower()
        text_data = text_data.split()
        wl = WordNetLemmatizer()
        text_data = [wl.lemmatize(word) for word in text_data if not word in set(stopwords.words('english'))]
        text_data = ' '.join(text_data)
        corpus.append(text_data)

    def second_viz(self):
        pass

    def third_viz(self):
        pass
