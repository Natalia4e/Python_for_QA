#Пользователь вводит данные. Сделайте проверку данных
#и преобразуйте если возможно в один из вариантов ниже:
#Целое положительное число
#Вещественное положительное или отрицательное числ
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в нижнем регистре в остальных случаях

text = input("Введите что-то...")
if text.isdigit():
    result = f'Вы ввели число {text}'
elif text.replace('-', '').replace('.', '').isdigit():
    result = f'Вы ввели ввели вещественное число {float(text)}'
elif len ([ i for i in text if i.isupper()]) > 0:
    result = f'У вас в тексте есть заглавные буквы {text.upper()}'
else:
    result = f'У вас в тексте нет заглавных букв {text}'
print(result)