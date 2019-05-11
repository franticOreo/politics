import re
import collections
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud

import os

text = re.sub('<[^<]+>', "", open("Senate_2019_04_02_7034_Official.xml").read())

with open("output.txt", "w") as f:
    f.write(text)

remove_white_space = re.sub('\s{2,}', " ", open("output.txt").read())

with open("speach.txt", "w") as f:
    f.write(remove_white_space)

data = open('speach.txt').read().lower()
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)

wordsFiltered = []

for w in words:
    if w not in stopWords and re.match( r'\w{3}', w):
        wordsFiltered.append(w)

freq = dict(Counter(wordsFiltered).most_common(1000))
# print(freq)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Generate a word cloud image
wordcloud = WordCloud(font_path='C:/Users/admin/Downloads/helvetica-2-cufonfonts/Helvetica.ttf', colormap='plasma', background_color='white').generate_from_frequencies(freq)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=60).generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
