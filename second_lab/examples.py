import nltk
from nltk.book import *
"""
Сортируется по алфавиту генерируемый список слов из множества
созданного из text7, которые отвечают
требованиям: в слове есть '-' и 'in-dex'
"""
print(sorted([w for w in set(text7) if '-' in w and 'in-dex' in w]))
"""
Сортируется по алфавиту генерируемый список слов из множества
созданного из text3, которые отвечают
требованиям: слово начинается с заглавной и > 10 букв
"""
print(sorted([w for w in set(text3) if w.istitle() and len(w) > 10]))
"""
Сортируется по алфавиту генерируемый список слов из множества
созданного из sent7, которые отвечают
требованиям: слово НЕ состоит только из прописных бука
"""
print(sorted([w for w in set(sent7) if not w.islower]))
"""
Сортируется по алфавиту генерируемый список слов из множества
созданного из text2, которые отвечают
требованиям: слово содержит 'cie' или 'cei'
"""
print(sorted([t for t in set(text2) if 'cie' in t or 'cei' in t]))

V = set(text1)
long_words = [w for w in V if len(w) > 12] # запись слов длинее 12 символов
print(sorted(long_words))
