import random
from random import randint


def get_unique_list_numbers() -> list[int]:
    shell = set()
    while len(shell) < 15:
        shell.add(randint(-10, 10))
    list_ = list(shell)
    random.shuffle(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# TODO написать функцию для получения списка уникальных целых чисел
