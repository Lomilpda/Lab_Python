sentence = 'she sell sea shells by the sea shore'
sentence = sentence.split()
for word in sentence:
    if len(word) > 4:
        print(word)
