#Cоздайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
import random

my_list = [random.randint(0,10) for _ in  range(20)]
print(*my_list)
my_set = set(my_list)
print(*my_set)
for i in my_set:
    if my_list.count(i) >= 2:
        my_list.remove(i)
        my_list.remove(i)
print(*my_list)