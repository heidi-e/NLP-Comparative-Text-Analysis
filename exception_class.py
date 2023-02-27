from Sentiment_NLP import SentimentNLP

class NLPError(Exception):
    """ A user-defined exception for signalling a
        grading application-specific issue """

    def __init__(self):
        super().__init__("Can't build Data dict")
        self.data = defaultdict(dict)

    def _default_parser(self, filename):
        """ Creates generic parser for simple text files
        """

        try:

            assert type(filename) == str, 'Expecting a file name'
            assert filename.endswith('.txt'), 'Not a txt file'

        except AssertionError as ae:
            print("Parser error: ", str(ae))
            return None

        except Exception as e:
            print("Parser Exception: " + str(e))
            return None

        else:
            print('Success')

        finally:
            print('CLOSING CONNECTION')

    def preprocess(self, content):

        try:
            assert type(content) == str, 'Expecting string'

    def _save_results(self, label, results):

        try:
            assert type(label) == str, 'Label not a string'
            assert type(results) == dict, 'Data not a dictionary'

        except AssertionError as ae:
            print("Parser error: ", str(ae))
            return None

        else:
            print('Success')

        finally:
            print('CLOSING CONNECTION')

    def load_text(selfself, filename, label=None, parser=None):

        try:
            assert type(filename) == str, 'Filename not a string'
            assert filename.lower().endswith('.txt', '.json', '.csv'), 'Not a valid file'
            assert type(label) == str, 'Label not a string'
            assert type(parser) == str, 'Parser not defined'

        except AssertionError as ae:
            print("Parser error: ", str(ae))
            return None

        else:
            print('Success')

        finally:
            print('CLOSING CONNECTION')

    def get_wordcount(self, word_list, k):

        try:
            assert type(word_list) == list, 'Not a list'
            assert type(k) == int, 'k not an integer'

        except AssertionError as ae:
            print("Parser error: ", str(ae))
            return None

        else:
            print('Success')

        finally:
            print('CLOSING CONNECTION')

    def wordcount_sankey(self, word_list, k):

        try:
            assert type(word_list) == list, 'Not a list'
            assert type(k) == int, 'k not an integer'

        except AssertionError as ae:
            print("Parser error: ", str(ae))
            return None

        else:
            print('Success')

        finally:
            print('CLOSING CONNECTION')