# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.


list_1 = [1, 4, 6, 7]
def summ_of_index (list_, start_, stop_):
    start_stop = sorted([start_, stop_])
    print(start_stop)
    return sum(list_[start_stop[0]:start_stop[1]])
print(summ_of_index(list_1, 1, 99))
