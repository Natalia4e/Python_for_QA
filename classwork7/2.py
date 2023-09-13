# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.
import string
from random import randint, sample


num_of_names = randint(3,10)
vowels = 'aeiouy'
def write_name_in_file():
    names = []
    while len(names) < num_of_names:
        res = ''.join(sample(string.ascii_lowercase, randint(4,7))).title()
        print(res)
        if len(set(res) & set(vowels)) > 0:
            names.append(res)
            print(f'{names = }')
    with open ('file_names.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(names))

write_name_in_file()
