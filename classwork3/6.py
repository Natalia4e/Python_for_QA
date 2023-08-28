#Пользователь вводит строку текста. Вывести каждое слово с новой строки.
#✔ Строки нумеруются начиная с единицы.
#✔ Слова выводятся отсортированными согласно кодировки Unicode.
#✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки

user_text = input().split()
print(user_text)
user_text.sort()
print(user_text)
max_word = max(user_text, key=len)
print(len(max_word))

for i, item  in enumerate(user_text,1):
    print(f'{i}.{item:{len(max_word)}}')