"""1.	Дослідити зв’язки голонім-меронім для іменників.
Знайти іменники для демонстрації наступних зв’язків:
 member_meronyms(), part_meronyms(), substance_meronyms(),
 member_holonyms(), part_holonyms(), та substance_holonyms()."""
import nltk
from nltk.corpus import wordnet as wn
def strange_thing(word):    # поиск голонимов и меронимов всех видов для всех списков синонимов (synsets)
    name = word # не будем перегружать word
    i = 0
    list_synsets = wn.synsets(word)
    for synset in list_synsets:
        mbr_hln = [synset.member_holonyms(), 'member_holonyms']
        prt_hln = [synset.part_holonyms(), 'part_holonyms']
        sbst_hln = [synset.substance_holonyms(), 'substance_holonyms']
        mbr_mrn = [synset.member_meronyms(), 'member_meronyms']
        prt_mrn = [synset.part_meronyms(), 'part_meronyms']
        sbst_mrn = [synset.substance_meronyms(), 'substances_meronyms']
        total = [mbr_hln, prt_hln, sbst_hln, mbr_mrn, prt_mrn, sbst_mrn]
        for list in total:
            if list.index != 1 and len(list[0]) >= 1:    # убираем из списка перебора текстовые блоки и synsets без результатов
                print(name, 'synset number'+' ', i, '\n')
                print(list[0], ':  ', list[1], '\n')
            else:
                pass
        i += 1
strange_thing('oil')
strange_thing('milk')
strange_thing('silk')
strange_thing('dog')
strange_thing('pole')
