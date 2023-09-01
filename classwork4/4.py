# Функция принимает на вход три списка одинаковой длины:
#✔ имена str,
#✔ ставка int,
#✔ премия str с указанием процентов вида «10.25%».
#✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

names = ['Vasya', 'Petya', 'Maria']
stavka = [44, 111, 228448]
bonus = ['10.25%', '25%', '5%']
def hr_info(names_, stavka_, bonus_):
    return {names_[i]: stavka_[i] + float(bonus_[i][:-1])/ 100 for i in range(len(names_))}

print(hr_info(names, stavka, bonus))
