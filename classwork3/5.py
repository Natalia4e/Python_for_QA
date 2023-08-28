# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.
import random

my_list = [random.randint(0,10) for _ in  range(20)]
random.seed(17)
print(*my_list)
res = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 1:
        res.append(i+1)
print(res)