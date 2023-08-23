есть дз есть не решенные задачи:
дз 1:
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from ctypes.wintypes import tagMSG
import copy

# Словарь вещей
THINGS_DICT = {"вилка": 1,
               "ложка": 1,
               "вода": 3,
               "ботинки": 3,
               "куртка": 5,
               "камера": 4,
               "чайник": 4,
               "палатка": 12,
               "еда": 5,
               "джинсы": 4,
               "посуда": 2,
               }
# Размер рюкзака
BAG_SIZE = 5


def bag_pack(things: dict[str, int], bag_volume: int, mode_greed=True) -> list[int | set]:
    """'Жадный' или 'Щедрый' рюкзак - забирает вещи пока есть место.
    В жадном режиме заполняет начиная с вещей от большего веса к меньшему,
    в щедром - наоборот, заполнение ведется от вещей с наименьшим весом.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    :mode_greed: режим работы True - жадный, False - щедрый
    """
    tmp_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=mode_greed))
    things_list: [int | set] = [0, set()]  # первый элемент - занятый размер, остальное - уложенные вещи
    # пока не наполнен рюкзак
    for t_key, t_val in tmp_dict.items():
        if (things_list[0] + t_val) <= bag_volume:
            things_list[1].add(t_key)
            things_list[0] += t_val

    return things_list


def bag_all_pack(things: dict[str, int], bag_volume: int) -> list:
    """Поиск всех вариантов упаковки.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    """
    bag_list: list[list[int | set]] = []
    best_case = 0
    # отобрать только подходящие вещи
    for t_key, t_val in things.items():
        # пропустить - если вещь не влазит в рюкзак
        if t_val <= BAG_SIZE:
            tmp_list = []
            for x in bag_list:
                # пропустить, если добавление невозможно к существующему набору
                weight = x[0] + t_val
                if bag_volume >= weight and not x[1].issubset(t_key):
                    y: list[int | set] = copy.deepcopy(x)
                    y[0] += t_val
                    y[1].add(t_key)
                    tmp_list.append(y)
                    if weight > best_case:
                        best_case = weight
            if len(tmp_list):
                for t in tmp_list:
                    bag_list.append(t)
            if bag_volume >= t_val:
                bag_list.append([t_val, {t_key}])
                if t_val > best_case:
                    best_case = t_val

    bag_list = list(filter(lambda b: b[0] == best_case, bag_list))
    return bag_list


def print_bag(bag: list[int | set]):
    """Вывод содержимого рюкзака."""
    for x in bag:
        if isinstance(x, int):
            print(f"Взято {x}", end=" | ")
        else:
            print(f"{x}")


def main():
    print(f"Размер рюкзака - {BAG_SIZE}")
    print("Перечень вещей:")
    print(THINGS_DICT)
    print("Жадный алгоритм:")
    print_bag(bag_pack(THINGS_DICT, BAG_SIZE))
    print()
    print("Щедрый алгоритм:")
    print_bag(bag_pack(THINGS_DICT, BAG_SIZE, False))
    print()
    print("Все наилучшие варианты:")
    for x in bag_all_pack(THINGS_DICT, BAG_SIZE):
        print_bag(x)


if __name__ == "__main__":
    main()
  -----
дз 2:
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# список для обработки
WORKING_LIST_1 = [1, 1, 2, 3, "F", "T", "F", 3, "o", "0", 0]
WORKING_LIST_2 = [1, 2, 3, 4, "F", "K", "X", "X", "0", 0, 8]


# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")
    print(f"{WORKING_LIST_2} - {double_items(WORKING_LIST_2)}")


if __name__ == "__main__":
    main()
  -------
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
from typing import Dict, Any

# Текст для обработки ресурс https://www.blindtextgenerator.com/lorem-ipsum
WORK_TEXT = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born " \
            "and I will give you a complete account of the system, and expound the actual teachings of the great " \
            "explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids " \
            "pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure " \
            "rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or " \
            "pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances " \
            "occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of " \
            "us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has " \
            "any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, " \
            "or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with " \
            "righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of " \
            "the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to " \
            "ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the " \
            "same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to " \
            "distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our " \
            "being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in " \
            "certain circumstances and owing to the claims of duty or the obligations of business it will frequently " \
            "occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always " \
            "holds in these matters to this principle of selection: he rejects pleasures to secure other greater " \
            "pleasures, or else he endures pains to avoid worse pains.But I must explain to you how all this " \
            "mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account " \
            "of the system, and expound the actual teachings of the great explorer of the truth, the master-builder " \
            "of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but " \
            "because those who do not know how to pursue pleasure rationally encounter consequences that are " \
            "extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, " \
            "because it is pain, but because occasionally circumstances occur in which toil and pain can procure " \
            "him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical " \
            "exercise, except to obtain some advantage from it? But who has any right to find fault with a man who " \
            "chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain"

# кол-во требуемых слов
FREQUENT_COUNT = 10


# Возврат count_words самых часто используемых слов из текста в виде строки, разделенных пробелами
def most_frequent_words(text: str, count_words: int) -> dict:
    # удалить знаки препинания, привести к единому регистру, тире ищем только как знак препинания,
    # дефис разделяющий части слова - является его частью
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    # подсчитываем кол-во слов, используем словарь для этого
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    # сортируем словарь по значениям, отбираем только нужное количество
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()
