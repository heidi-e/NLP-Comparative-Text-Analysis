def third_viz(self):
    """
    creates word cloud visualization based on text content from all the files
    """

    text_content = self.data['raw_text']

    # combine all the contents of the text files together
    value = ','.join(text_content.values())

    # Create and generate a word cloud image
    wordcloud = WordCloud(background_color="white").generate(value)

    # Display the generated image
    plt.figure(figsize=[20, 10])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title('all text files', fontsize=40)
    plt.axis("off")
    plt.show()