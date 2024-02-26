# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

from random import randint


def isFerzi(f1: list, f2: list, f3: list, f4: list, f5: list, f6: list, f7: list, f8: list) -> bool:
    list_ferzi = [f1, f2, f3, f4, f5, f6, f7, f8]
    print(list_ferzi)
    for i in range(8):
        for j in range(i + 1, 8):
            if list_ferzi[i][0] == list_ferzi[j][0] or list_ferzi[i][1] == list_ferzi[j][1] \
               or abs(list_ferzi[i][0] - list_ferzi[j][0]) == abs(list_ferzi[i][1] - list_ferzi[j][1]):
                return False
    return True


def ferzi_generate():
    ferzi_list = []
    count = 0
    while count < 4:
        f1, f2 = [1, randint(1, 8)], [2, randint(1, 8)] 
        f3, f4 = [3, randint(1, 8)], [4, randint(1, 8)] 
        f5, f6 = [5, randint(1, 8)], [6, randint(1, 8)] 
        f7, f8 = [7, randint(1, 8)], [8, randint(1, 8)] 
        if isFerzi(f1, f2, f3, f4, f5, f6, f7, f8):
            ferzi_list.append([f1, f2, f3, f4, f5, f6, f7, f8])
            count += 1
    return ferzi_list
