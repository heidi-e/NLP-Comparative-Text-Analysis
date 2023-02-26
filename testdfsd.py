import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Create your word cloud data for each subplot
text1 = "some text for wordcloud 1"
text2 = "some text for wordcloud 2"
text3 = "some text for wordcloud 3"

# Create a list of word cloud data
text_list = [text1, text2, text3]

# Create the figure and subplots
fig, axs = plt.subplots(1, len(text_list), figsize=(15, 5))

# Create a word cloud for each subplot
for i in range(len(text_list)):
    ax = axs[i]
    wc = WordCloud().generate(text_list[i])
    ax.imshow(wc, interpolation='bilinear')
    ax.set_axis_off()

# Adjust the layout
plt.tight_layout()
plt.show()
