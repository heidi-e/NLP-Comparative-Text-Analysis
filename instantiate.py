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

# create sankey diagram
#object.wordcount_sankey()

# create word cloud visualization
object.second_viz()

# create multiple bar plot
#object.third_viz()







