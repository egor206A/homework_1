есть что не успели есть дз:
дз 1:
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# Выделение целой части после операции не производим. Получаемую от пользователя информацию считаем корректной

import fractions


def main():
    fract_1 = get_str("Введите 1-ю дробь: ")
    fract_2 = get_str("Введите 2-ю дробь: ")

    print("Мои методы:")
    print(f"{fract_1} + {fract_2} = {fract_sum(fract_1, fract_2)}")
    print(f"{fract_1} * {fract_2} = {fract_milt(fract_1, fract_2)}")

    print("Проверочные методы:")
    print(f"{fract_1} + {fract_2} = {fractions.Fraction(fract_1) + fractions.Fraction(fract_2)}")
    print(f"{fract_1} * {fract_2} = {fractions.Fraction(fract_1) * fractions.Fraction(fract_2)}")


# сумма дробей
def fract_sum(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # ищем НОК, приводим к общему знаменателю
    fract_lcm = my_lcm(fract_1_part[1], fract_2_part[1])
    # добавочные множители для приведения к единому знаменателю
    mult_1 = int(fract_lcm / fract_1_part[1])
    mult_2 = int(fract_lcm / fract_2_part[1])
    fract_1_part = [i * mult_1 for i in fract_1_part]
    fract_2_part = [i * mult_2 for i in fract_2_part]
    # сложение дроби
    fract_1_part[0] += fract_2_part[0]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# приведение дроби из строкового представления к списку чисел
# [числитель, знаменатель]
def split_fraction(fract: str) -> list:
    fraction_parts = fract.split("/")
    fraction_parts = [int(s) for s in fraction_parts]
    return fraction_parts


# произведение дробей
def fract_milt(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # умножение дробей
    fract_1_part[0] *= fract_2_part[0]
    fract_1_part[1] *= fract_2_part[1]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# Поиск НОД
def my_gcd(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    while num_2:
        num_1 %= num_2
        num_1, num_2 = num_2, num_1

    return int(num_1)


# Поиск НОК
def my_lcm(num_1: int, num_2: int) -> int:
    return int(num_1 / my_gcd(num_1, num_2) * num_2)


# Запрос строковой величины
def get_str(message: str = None) -> str:
    if message is None:
        message = "Введите строку: "
    return input(message)


# Старт
if __name__ == "__main__":
    main()
  ------
дз2:
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

# В ходе работы пользователю необходимо ввести несколько целых чисел.
# Ввод осуществляется до ввода отрицательного значения.
# На основе введенных чисел формируется список, значения из которого
# в последствии конвертируются из 10-й в 16-ю систему счисления.

BASE_HEX = 16  # основание системы счисления в которую переводим
BASE_DEC = 10  # основание системы счисления из которой переводим
ASCII_START = 55  # стартовый код для отображения (A-F)


def main():
    number: int
    numbers = []

    print('Введите числа для перевода в HEX.\n'
          'Отрицательное число - завершить ввод')
    while True:
        number = get_int('Введите число: ')
        if number < 0:
            break
        numbers.append(number)

    print(' число | моя функция | heh() ')
    print('-----------------------------')
    for i in numbers:
        print(f" {i:<5} | {dec_to_heh(i):11} | {hex(i)}")


# перевод числа в 16-ричное представление
def dec_to_heh(dec_num: int) -> str:
    hex_num: str = ""

    while dec_num:
        div_mod = dec_num % BASE_HEX
        hex_num = (chr(div_mod + ASCII_START) if div_mod >= BASE_DEC else str(div_mod)) + hex_num
        dec_num //= BASE_HEX

    return '0x' + (hex_num if hex_num else "0")


# Запрос численной величины
def get_int(message: str = None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
  --------
Задание 6
Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash*percent_take < 30:
        bank -= 30
        print("списаны проценты за cash: ", 30)
    elif cash*percent_take > 600:
        bank -= 600
        print("списаны проценты за cash: ", 600)
    else:
        bank -= cash * percent_take
        print("списаны проценты за cash: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:

            return cash


while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 -выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        add_bank(check_bank())
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '3':
        print("Баланс = ", bank)
    else:
        exit_bank()
