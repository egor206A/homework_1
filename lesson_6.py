есть дз и есть не решенные задачи:
----
дз1:
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from typing import Tuple

# Имена файлов для отображения
FILE_1 = "d:\\path1\\sub_path1\\file_1.png"
FILE_2 = "d:\\path2\\sub_path2\\file_2.txt"
FILE_3 = "d:\\path3\\sub_path3\\file_3.docx"


def split_path(path: str) -> tuple[str, str, str]:
    """Парсинг абсолютного пути на каталог, имя и расширение файла"""
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(FILE_1))
    print(split_path(FILE_2))
    print(split_path(FILE_3))


if __name__ == "__main__":
    main()
  ------
дз2:
# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# Списки для проверки работы генератора
NAMES = ["Иван", "Петр", "Михаил", "Сергей"]
RATES = [10_000, 20_000, 15_000, 30_000]
PERCENTS = ["10.25%", "15.00%", "6.50%", "12.75%"]


def gen_dict(names: list[str], rates: list[int], percents: list[str]):
    """Генератор премий"""
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, rates, map(lambda x: float(x[:-1]), percents))))}


def main():
    print(NAMES)
    print(RATES)
    print(PERCENTS)
    print(*gen_dict(NAMES, RATES, PERCENTS))


if __name__ == "__main__":
    main()
  -------
дз3:
# Генератор чисел Фибоначчи
# Последовательность Фибоначчи - 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Множество для проверки генерации рядов Фибоначчи
FIB_SET = (5, 8, 10, 15)


def fib_gen(n: int) -> list[int]:
    """Генератор чисел Фибоначчи"""
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    for n in FIB_SET:
        print(*fib_gen(n))


if __name__ == "__main__":
    main()
-------
Задача 7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

'''


from my_pacage_task8.module_task7 import calend

if __name__ == '__main__':
    print(calend('12.12.2016'))
    print(calend('29.02.2016'))
