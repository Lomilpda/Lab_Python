start_string = 'Pinchuk Alexey Vladimirovich'
start_string = start_string.lower()
vowel_letters = ['a','e','i','o','u','y']
result = []
start_string = start_string.split()
for word in start_string:
    for char in word:
        if char in vowel_letters:
            pass
        else:
            result.append(char)
print(result)
input()