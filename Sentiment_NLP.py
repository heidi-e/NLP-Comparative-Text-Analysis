import pandas as pd
from typing import List
from collections import Counter, defaultdict
import random
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pprint as pp
from sankey_test import make_sankey
from nltk.sentiment import SentimentIntensityAnalyzer

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
        :param filename (str): name of file
        :return: a dict of top five most freq used words in that file
        """
        # read in txt file into string
        with open(filename) as f:
            content = f.read()

        # pre-process the content
        content = self.preprocess(content)

        # this results dict will have the statistics and stuff for each file, no need to save the actual string
        # We need wordcount,
        wordcounts = SentimentNLP.count(content)

        results = {
            'wordcount': wordcounts,
            'sentiment': 20,
        }
        return results

    def preprocess(self, content):
        """

        :param content (str): the contents of the file
        :return: text_data (str): cleaned version of content
        """
        # this takes out punctuation, lower cases everything, combined similar words, takes out stop words/ non-words.
        text_data = content
        text_data = re.sub('[^a-zA-Z]', ' ', text_data)
        text_data = text_data.lower()
        text_data = text_data.split()
        wl = WordNetLemmatizer()
        text_data = [wl.lemmatize(word) for word in text_data if not word in set(stopwords.words('english'))]
        text_data = ' '.join(text_data)

        return text_data

    def count(content):
        """
        counts the number of words and appends into a dictionary
        takes in a parsed/cleaned string from txt file
        content (str): the contents of the file
        return: top_five_dict (dict): top five word count dictionary with key as word and value as word counts
        """
        counts = dict()
        words = content.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        """top_five_values = sorted(counts.values(), reverse=True)[:5]
        top_five_dict = {k: v for k, v in counts.items() if v in top_five_values}"""

        return counts

    def _save_results(self, label, results):
        """ Integrate parsing results into internal state
        label (str): unique label for a text file that we parsed
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

        # pp.pprint(self._save_results())

    def load_stop_words(self, stopfile):
        """

        :param stopfile:
        :return:
        """
        pass

    def get_wordcount(self, word_list = None, k = 5):
        """

        :param word_list:
        :param k:
        :return:
        """
        if word_list == None:
            wordcount_dict = self.data["wordcount"]

            for filename in wordcount_dict:

                temp_dict = dict(sorted(wordcount_dict[filename].items(), key=lambda x: x[1], reverse=True)[:k])
                wordcount_dict[filename] = temp_dict

        else:
            wordcount_dict = self.data["wordcount"]

            for filename in wordcount_dict:
                temp_dict = defaultdict(dict)
                for key, value in wordcount_dict[filename].items():
                    if key in word_list:
                        temp_dict[key] = value

                wordcount_dict[filename] = temp_dict


        self.data["wordcount"] = wordcount_dict



    def wordcount_sankey(self, word_list=None, k=5):
        """

        :param word_list:
        :param k:
        :return:
        """

        self.get_wordcount(word_list, k)

        df_sankey = pd.DataFrame(columns=['text', 'word'])
        wordcount_dict = self.data["wordcount"]

        for filename in wordcount_dict:
            for key, value in wordcount_dict[filename].items():
                for i in range(value):
                    new_row = {'text': filename, 'word': key}
                    df_sankey = df_sankey.append(new_row, ignore_index=True)

        make_sankey(df_sankey, df_sankey.columns, 0)


    def second_viz(self):
        pass

    def third_viz(self):
        pass

    def clean_data(self):
        pass
