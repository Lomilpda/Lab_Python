import nltk
from nltk.book import *
text = text6
upper_words = sorted([word for word in text if word.isupper() is True])
print(upper_words)
