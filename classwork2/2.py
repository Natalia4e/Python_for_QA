# Создайте в переменной data список значений разных типов, перечислив их через запятую внутри квадратных скобок
# Для каждого элемента в цикле выведете :
# порядковый номер, начиная с 1
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число, только если он положительный
# результат  проверки на строку , только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результат
import sys
data = [1, 2.45, "hi", True, False, 1, True, (1,2)]

for i in range(len(data)):
    print(i+1)
    print(data[i])
    print(id(data[i]))
    print(sys.getsizeof(data[i]))
    print(hash(data[i]))
    if isinstance(data[i], int):
        print(isinstance(data[i], int))
    if isinstance(data[i], str):
        print(isinstance(data[i], str))
    print ("_________")




