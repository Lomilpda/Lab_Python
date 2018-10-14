import nltk
import matplotlib
from nltk.book import *
text = text5
result_text = []
for word in text:
    if len(word) > 4:
        result_text.append(word)
print(result_text)
frequency_analisis = FreqDist(result_text)
frequency_analisis.tabulate()
frequency_analisis.plot(100)
