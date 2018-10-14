import nltk
from nltk.book import *
text = text6
result_list = [word for word in text if (word.endswith('ize') and 'z' in word and 'pt' in word and word.isupper())]  # а это точно одно условие?
print(result_list)
