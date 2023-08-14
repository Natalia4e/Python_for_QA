# Решите квадратное уравнение 5x2 -10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.
a, b, c = 5, -10, -400
discriminant = b**2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + discriminant ** 0.5)/(2*a)
    x2 = (-b - discriminant ** 0.5)/(2*a)
    print(x1, x2)
elif discriminant == 0:
    x = -b / (2*a)
    print(x)
else:
    print("Корней нет")

#Посчитайте сумму чётных элементов от 1 до n исключая кратные e, Используйте while и if

e, n = int(input("Введите число e: ")), int(input("Введите число n: "))
i = 0
summ = 0
while i < n:
    if i % 2 == 0 and i % e != 0:
        summ += i
    i += 1
print(summ)

# Напишите программу, которая запрашивает год и проверяет его на високосность.

year = int(input("Введите год: "))
res = None
if year % 4 == 0:
    if year % 400 == 0:
        res = "Твой год високосный"
    elif year % 100 != 0:
        res = "Твой год не високосный"
    else:
        res = "Твой год високосный"
else:
    res = "Твой год не високосный"

print(res)

