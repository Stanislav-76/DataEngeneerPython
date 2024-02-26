# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from module2 import guess_riddle


def list_riddles():
    my_dict = {'Ночью от не любит спать. Ему хочется гулять'
               'Молоко из плошки пьет. Это наш любимый ...': ['кот', 'динозавр', 'лев', 'медведь', 'страус'],
               'Без окон и дверей полна горница людей': ['кот', 'огурец', 'слива', 'школа', 'кино']}
    for k, v in my_dict.items():
        gess_riddle1 = guess_riddle(k, v, 5)
        print(gess_riddle1)
        yield k, gess_riddle1


if __name__ == "__main__":
    list_riddles()
