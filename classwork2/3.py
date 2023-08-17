#Напишите программу, которая получает целое число и возвращает
#его двоичное, восьмеричное строковое представление.
#✔ Функции bin и oct используйте для проверки своего
#результата, а не для решения.

num = int(input("Введите число: "))
res_8 = ""
res_2 = ""
num1 = num2 = num
while num1 > 0:
    res_2 = str(num1 % 2) + res_2
    num1 //= 2
print(res_2, bin(num).replace("0b",''))
while num2 > 0:
    res_8 = str(num2 % 8) + res_2
    num2 //= 8
print(res_8, oct(num).replace('0o',''))

