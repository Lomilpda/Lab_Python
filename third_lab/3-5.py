"""5.	Який відсоток синсетів іменників не мають гіпонімів? До всіх
 синсетів можна доступитися
 за допомогою wn.all_synsets('n').  """
from nltk.corpus import wordnet as wn
list_synsets = []
no_hyponims_list = []
for word in wn.all_synsets('n'):
    list_synsets.append(word)
    val = word.hyponyms()
    if len(val) ==0:
        no_hyponims_list.append(word)
print(len(no_hyponims_list)/len(list_synsets)*100, ' %')
