# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
#Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь
from sys import argv
from random import randint
def guess(start, stop, tries):
    random_num = randint(start, stop)
    while tries > 0:
        user_num = int(input('Please input your number: '))
        if user_num == random_num:
            print('You are lucky!')
            break
        elif user_num > random_num:
            print('My number is less')
        else:
            print('My number is bigger')
        tries -= 1
    else:
        print(f"Game over. Number was {random_num}")

#guess(0, 100, 6)

argv = list(map(int, argv[1:]))
guess(*argv)
