есть дз  и есть не решенные задача:
дз1:
"""Модуль проверки расстановок на шахматной доске

Ферзь бьет фигуру, если она находиться на одной с ним вертикали, горизонтали или диагонали
Ситуацию указания двух ферзей на одной клетке не обрабатываем
"""
import random as rnd

__all__ = ['check_queen_8x8', 'gen_positions']

_QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
_SIZE_BOARD: int = 8  # размер доски


def check_queen_8x8(positions: list[tuple]) -> bool:
    """Проверка задачи о ферзях.

    :positions: позиции ферзей - кортежи (строка, столбец)
    """
    result = True

    if len(positions) != _QUEEN_COUNT:
        result = False
    else:
        for i in range(_QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, _QUEEN_COUNT):  # проверяем со следующими до конца списка
                row_2, col_2 = positions[j]
                # Ферзи на одной линии, если координаты строки или столбца у них равны.
                # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
                # количество строк и столбцов в любую из сторон
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def gen_positions() -> list[tuple[int, int]]:
    """Генератор позиций ферзей. Генерирует _QUEEN_COUNT позиций, по одному ферзю на строку.
    Для доски размером _SIZE_BOARD
    """
    result = []
    for i in range(_SIZE_BOARD):
        result.append((i, rnd.randint(0, _SIZE_BOARD - 1)))
    return result
    -------
    дз2:
    from datetime import datetime
from sys import argv

__all__ = ['check_year', 'date_validator']

def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date_for_check: str) -> str:
    if check_year(date_for_check):
        return 'Високосный' if _check_leap_year(date_for_check) else 'Не является високосным'
    else:
        return f'Дата заполнена некорректно'


if __name__ == "__main__":
    if len(argv) == 2:
        _, date = argv
        print(date_validator(date))
    else:
        print("Дата для проверки не указана!")
        -------
        дз3:
        # 2. напишите код, решающий задачу о 8 ферзях!
# - Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# - Вам дана расстановка 8 ферзей на доске,
# - определите, есть ли среди них пара бьющих друг друга.
# - Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# - Если ферзи не бьют друг друга верните истину, а если бьют - ложь

# 3. Напишите функцию в шахматный модуль!
# - Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# - Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import func_queens
import queens_true
import random_queens

# Вызов функции с правильной расстаовкой ферзей
# func_queens.intersection_search(queens_true.queens)

# Вызов функции нахождения пересечений ферзей
func_queens.intersection_search(random_queens.queens_rnd())

# нахождение четырёх правильных расстановок ферзей
# с помощью рандомной расстановки ферзей и записи в файл .txt
# func_queens.func_search_four_arrangements()
        '''
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''

from typing import Generator

def primes(n: int) -> Generator:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for num, i in enumerate(primes(100), start=1):
    print(f'{num} = {i}')

# Пример отличие return (обычной функции)от yield (функции-генератора)
from typing import Generator


def p(n) -> int:
    for i in range(n):
        return i

def p1(n) -> Generator:
    for i in range(n):
        yield i             # запоминает значение i и каждый раз при вызове функции начитнает соследующего значения i
        print('yield следующий')

gen = p1(10)        # кол значений не должно быть больше 10 иначе выбрасывает исключение при привышении кол генерации

for i in range(10):
    print('return ', p(10))
    print('yield   ', next(gen))
