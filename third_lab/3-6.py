"""6.	Визначити функцію supergloss(s) , яка буде приймати синсет
s як аргумент і повертати стрічку в якій будуть поєднані всі описи
всіх значень синсету s та описи всіх  гіпернімів та гіпонімів s."""
import nltk
from nltk.corpus import wordnet as wn
def supergloss(s):
    synset_list = wn.synset(s)
    result = [synset_list.definition(), synset_list.hypernyms(), wn.synset(s).hyponyms()] #hypernyms - обобщение, hyponym - детализация
    return result
print(supergloss('magnet.n.01'))

