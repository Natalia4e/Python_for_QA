# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег


def add_money(balance):
    balance = luxury_tax(balance)
    transaction = int(input("Введите сумму которую хотите положить на счет : "))
    if transaction % 50 == 0 and transaction > 0:
        balance += transaction
    else:
        print('Сумма пополнения и снятия должны быть кратны 50 у.е.')
    return balance

def cash_withdrawal(balance):
    balance = luxury_tax(balance)
    withdrawal = int(input("Введите сумму которую хотите снять : "))

    if withdrawal > balance:
        print('Нельзя снять больше, чем на счёте')
        return balance

    if withdrawal < 0 or withdrawal % 50 != 0:
        print('Сумма пополнения и снятия должны быть кратны 50 у.е.')
        return balance

    comission = withdrawal * 0.015

    if comission < 30:
        comission = 30

    if comission > 600:
        comission = 600

    balance = balance - withdrawal - comission
    return balance

def luxury_tax(balance):
    if balance > 5000000:
        balance = balance - (balance * 0.1)
    return balance



def menu():
    balance = 0
    while True:
        print(balance)
        type_num = input("Choise\n"
                         "1 - пополнить счет\n"
                         "2 - снять деньги\n"
                         "3 - exit\n")
        match type_num:
            case "1":
                balance = add_money(balance)
                pass
            case "2":
                balance = cash_withdrawal(balance)
                pass
            case "5":
                logging.info("Stop program")
            case _:
                logging.error("ERROR")
                print("ERR")


menu()


