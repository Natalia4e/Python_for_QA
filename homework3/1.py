#Дан список повторяющихся элементов. Вернуть список
#с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [1,1,2,2,3,3,4,5,6,7]
duplicate_list = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicate_list:
        duplicate_list.append(item)
print(duplicate_list)