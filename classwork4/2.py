# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно
import shlex


def input_str(s):
    new_li = sorted(list(map(int, s.split())))
    new_dic = {chr(i): i for i in range(new_li[0], new_li[1]+1)}
    return new_dic

st = input("Please input your text: ")
print(input_str(st))