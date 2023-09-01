# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь

dict_companies = {'Lukoil': [44, 333, -100],\
                  'gazprom': [99, 0, -127363],\
                  'gb': [334, 244, 3554]}

def profit(dictionary):
    dict_ = list(map(lambda x: sum(dictionary[x]), dictionary))
    all_profit = all(list(map(lambda x: x > 0, dict_)))
    return all_profit

print(profit(dict_companies))