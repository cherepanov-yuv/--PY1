import string
import random

alphabet = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)  # задаем алфавит пароля


def get_random_password() -> str:
    length = int(input("Введите длину пароля: "))  # длина пароля от пользователя

    if length == 0:
        length = 8  # если пользователь введет длину пароля равную "нулю", она по умолчанию будет равна 8

    password = []
    for i in range(length):
        password.append(random.choice(alphabet))  # выбор случайных символов из списка
        # используя функцию choice - увеличивает количество комбинаций за счет дублирования символов

    return "".join(password)  # преобразование списка в строку и вывод строки


print(get_random_password())  # вызов функции
# TODO написать функцию генерации случайных паролей
