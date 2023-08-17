#Напишите программу, которая вычисляет площадь
#круга и длину окружности по введённому диаметру.
#✔ Диаметр не превышает 1000 у.е.
#✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal
from math import pi
num = -1
decimal.getcontext().prec = 42
num = decimal.Decimal(input('Введите число'))

while num < 0 or num > 1000:
    num = decimal.Decimal(input("Введите число превышающее 1000:"))
    print(num)
sq = decimal.Decimal(pi)*(num / 2) ** 2
dlina = decimal.Decimal(pi)* num
print(sq, dlina)