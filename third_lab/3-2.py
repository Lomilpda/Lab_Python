"""2.	Використовуючи компаративний словник знайти для німецької,
 італійської та англійської мов близькі слова. Чи можуть отримані
 результати використовуватися для здійснення перекладу?"""
from nltk.corpus import swadesh
print(swadesh.entries(['de', 'en', 'it']))
# ('lang', 'long', 'lungo') - длинный
# 'Nase', 'nose', 'naso' - нос
# 'Name', 'name', 'nome' - имя
