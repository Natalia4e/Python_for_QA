# Напишите функцию, которая заполняет файл (добавляет в конец)
# случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количествоx строк и имя файла передаются как аргументы функции.

from random import randint, uniform
min_size = - 1000
max_size = 1000

def write_in_file(num_of_str, file_name):
    with open (f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join([f'{randint(max_size,max_size)} | {uniform(min_size,max_size)}' for i in range(num_of_str) ]))

write_in_file(12, 'seminar_7_01')