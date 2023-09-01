# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def input_str():
    new_str = input("Please input your text: ")
    new_str = [ord(i) for i in set(new_str)]
    return sorted(new_str, reverse=True)

print(input_str())