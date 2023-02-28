from Sentiment_NLP import SentimentNLP
#from testing import SentimentNLP
import pprint as pp

object = SentimentNLP()

object.load_text('5_4.txt')
object.load_text('6_3.txt')
object.load_text('7_1.txt')
object.load_text('8_2.txt')
object.load_text('9_4.txt')

#pp.pprint(object.data)

#object.wordcount_sankey(word_list=["br", "darling", "ronald", "stage", "film", "actor"])

#object.wordcount_sankey()
object.wordcount_sankey()
object.second_viz()
object.third_viz()
object.fourth_viz()

#object.visualize(wordcount_sankey)





