def third_viz(self):
    """
    creates word cloud visualization based on text content from all the files
    """

    text_content = self.data['raw_text']
    text_list = []
    # combine all the contents of the text files together
    #value = ','.join(text_content.values())
    for key, value in text_content.items():
        text_list.append(value)

    # Create the figure and subplots
    fig, axs = plt.subplots(1, len(text_list), figsize=(15, 5))

    # Create a word cloud for each subplot
    for i in range(len(text_list)):
        ax = axs[i]
        wc = WordCloud(background_color="white").generate(text_list[i])
        ax.imshow(wc, interpolation='bilinear')
        ax.set_axis_off()

    # Adjust the layout
    plt.tight_layout()
    plt.show()


