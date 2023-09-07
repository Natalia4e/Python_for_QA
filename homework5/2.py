# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def calculate_bonus(names, wages, bonuses):
    result = {}
    for i in range(len(names)):
        name = names[i]
        wage = wages[i]
        bonus = bonuses[i]

        # Удаление знака процента и преобразование строки в число
        bonus_percent = float(bonus.rstrip('%'))

        # Вычисление итоговой суммы с учетом бонуса
        total_wage = wage * (1 + bonus_percent / 100)

        result[name] = total_wage

    return result


names = ['Мария', 'Андрей', 'Иван']
wages = [1000, 2000, 1500]
bonuses = ['10.25%', '20.15%', '15%']

result = calculate_bonus(names, wages, bonuses)
print(result)