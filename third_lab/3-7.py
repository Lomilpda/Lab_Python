"""
Модифікувати програму генерації випадкового тексту для виконання 
наступного: зберігати можливі наступні слова у списку та вибирати 
їх за допомогою random.choice() попередньо виконавши import random.
"""
import nltk
import random
sent = ['In', 'the', 'beginning', 'God', 'created', 'the',
        'heaven', 'and', 'the', 'earth', '.', 'some', 'magic',
        'will', 'be', 'great']
bigrams_list = list(nltk.bigrams(sent))
generated_text = []
i = 0
while i <= len(bigrams_list):
    generated_text.append([random.choice(bigrams_list)])
    i += 1
print(generated_text)
