# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.
# Продолжаем развивать задачу
# Возьмите словарь, который вы получили. Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

my_st = 'dhghkggerkj'
#Создайте из строки словарь, где ключ — буква, а значение — код буквы.
my_dict = {i: ord(i) for i in my_st}
print(my_dict)

my_iter = iter(my_dict.items())
for _ in range(5):
    print(next(my_iter))
print()
print(next(my_iter))