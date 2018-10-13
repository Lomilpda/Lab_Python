import nltk
from nltk.book import *
a = text1
'''
В первом варианте сортируется по алфавиту  элементы множества созданного из слов 
начинающихся с малой буквы в text1. Во втором варианте сортируются по алфавиту все слова начинающиеся с малой
буквы в множестве созданом из text1. Писать можно и так и так, результат тот же
'''
first = sorted(set([w.lower() for w in a]))
second = sorted([w.lower() for w in set(a)])
result = list(set(first) - set(second))
result2 = list(set(second)-set(first))
print(result, result2)
