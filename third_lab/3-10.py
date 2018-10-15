"""
10.	Полісемія - це явище коли одне слово має декілька значень
 ( іменник dog має 7 значень, кількість яких визначити можна як
 len(wn.synsets('dog', 'n'))). Знайдіть середнє значення полісемії
  для іменників.
"""
from nltk.corpus import wordnet as wn
polisemia = 0
print(len(list(wn.all_synsets('n'))))
list_synsets = [x for x in wn.all_synsets('n')]
print(list_synsets)
for word in list_synsets:
   polisemia = len(wn.synsets(word, 'n'))+polisemia #что-то тут не так
print(polisemia)
print(len(polisemia)/len(list_synsets))
