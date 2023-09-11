#Создайте модуль с функцией внутри.
# Функция получает на вход загадку,
# список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка
# или ноль, если попытки исчерпаны.
#Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
#Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.
import random
from random import choice

_result_dict = {}
def store_of_puzzles():
    dict_puzzle = {"Зимой и летом одним цветом": ['елка', 'ель', 'елочка'],
                   "Висит грушка нельзя скушать": ['лампа','лампочка'],
                   "Не лает не кусает , в дом не пускает": ['замок', 'замочек']}
    result = choice(list(dict_puzzle))
    print(result)
    return result, dict_puzzle[result]

def guess(count):
    for _ in range(count):
        puzzle, answers = store_of_puzzles()
        tries = random.randint(3,5)
        print(f'У тебя {tries} попыток')
        count = 0
        while count < tries:
            user_answer = input('Please input your answer: ')
            if user_answer in answers:
                print(f'Your are lucky ! Угадал с попытки номер {count + 1}\n')
                break
            else:
                print('Try again')
            count += 1
            print(f'У тебя осталось {tries - count} попыток\n')
        else:
            print(f"Game over. Answer was {answers[0]}")

def save_result(puzzle: str, tries: int):
    _result_dict[puzzle] = tries
def show_results():
    return '\n'.join([f'Загадка: {puzzle} jnuflfyf c {tries} попытки' for puzzle, tries in _result_dict.items()])

guess(4)
print(show_results())

