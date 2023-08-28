#Вручную создайте список с целыми числами, которые
#повторяются. Получите новый список, который содержит
#уникальные (без повтора) элементы исходного списка.

my_list_1 = [1,1,2,2,3,3,4,5,6,7]
unuque_list_1 = set(my_list_1)
print(unuque_list_1)

my_list_2 = [1,1,2,2,3,3,4,5,6,7]
unuque_list_2 = []
for item in my_list_2:
    if item not in unuque_list_2:
        unuque_list_2.append(item)
print(unuque_list_2)
