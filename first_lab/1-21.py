"""
21.	Напишіть програму, яка створить стрічку в якій будуть записані
 другі символи всіх слів з стрічки silly.
"""
silly = "newly formed bland ideas are inexpressible in an infuriating way"
silly = silly.split() # создаем из строки список, разделяя по пробелу
new_str = ''
for word in silly:  # перебор всех слов в списке
    if len(word) >= 2:  # проверяем что бы в слове было хотя бы 2 символа
        new_str = new_str + word[1:2] # перезаписываем строку добвляя второй символ в списке
    else:
        pass  # необязательно
print(new_str)
