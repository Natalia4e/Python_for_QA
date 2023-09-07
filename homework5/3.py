# Создайте функцию генератор чисел Фибоначчи

def fibonacci_numb(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
print(fibonacci_numb(10))