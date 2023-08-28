#✔ Создайте вручную кортеж содержащий элементы разных типов.
#✔ Получите из него словарь списков, где:ключ — тип элемента,
# значение — список элементов данного типа.

my_tu = (1, 2, 'Hello', 3.4, [2,3], 11, 5.5, 'world', [5,6], 7)
my_dict = {}
for i in my_tu:
     if type(i) not in my_dict:
         my_dict[type(i)] = [i]
     else:
         my_dict[type(i)].append(i)
print(my_dict)