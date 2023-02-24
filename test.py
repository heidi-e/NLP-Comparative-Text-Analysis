import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

with open('49924_0.txt') as f:
    content = f.read()
    print(content)

corpus = []
text_data = content
text_data = re.sub('[^a-zA-Z]', ' ', text_data)
text_data = text_data.lower()
text_data = text_data.split()
wl = WordNetLemmatizer()
text_data = [wl.lemmatize(word) for word in text_data if not word in set(stopwords.words('english'))]
text_data = ' '.join(text_data)
corpus.append(text_data)

print(text_data)


"""import csv
import pandas as pd

def main():





    data = pd.read_csv('transcript_data.csv')
    data['transcript'] = data['transcript'].str.split()
    data = data.explode('transcript').value_counts().reset_index(name='count')
    print(data)

main()



>>>>>>> ec30bf6 (test)
"""