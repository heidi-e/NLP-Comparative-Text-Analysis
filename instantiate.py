"""
This file can be used to run Sentiment_NLP
"""

from Sentiment_NLP import SentimentNLP



object = SentimentNLP()

object.load_text('Text_Files/michael-jackson.txt')
object.load_text('Text_Files/lorde.txt')
object.load_text('Text_Files/nirvana.txt')
object.load_text('Text_Files/rihanna.txt')
object.load_text('Text_Files/amy-winehouse.txt')


object.wordcount_sankey()

object.second_viz()

object.third_viz()







