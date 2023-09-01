# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

li = [ 1, 8, 12, 3, 5, 7]

def buble_sort(list_):
    for i in range(len(list_)):
        for j in range(i, len(list_)-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]

buble_sort(li)
print(li)