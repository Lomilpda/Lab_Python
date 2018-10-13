sentence = 'she sell sea shells by the sea shore'
sentence = sentence.split()
new_string = ''
for word in sentence:
    if word.startswith('se'):
        new_string = 'like'+word
        print(new_string)
