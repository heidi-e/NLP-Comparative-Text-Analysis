from Sentiment_NLP import SentimentNLP
#from testing import SentimentNLP
from exception_class import NLPError
import pprint as pp

object = SentimentNLP()

#object.load_text('5_4.txt', "label", "parser")

object.load_text('michael-jackson.txt')
object.load_text('lorde.txt')
object.load_text('notorious_big.txt')
object.load_text('rihanna.txt')
object.load_text('amy-winehouse.txt')

#pp.pprint(object.data)

#object.wordcount_sankey(word_list=["br", "darling", "ronald", "stage", "film", "actor"])


object.wordcount_sankey()

object.second_viz()

object.third_viz()
object.fourth_viz()

#object.visualize(wordcount_sankey)





