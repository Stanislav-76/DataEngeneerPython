# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def patcher(pathFile: str):
    a, b = os.path.split(pathFile)
    b, c = b.split('.')
    return (a, b, c)


pathFile = "C:\Учеба_GB\DataEngineer\Python\Sem5\Work1.py"
print(patcher(pathFile))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

list1 = ['vasily', 'petr', 'maria']
list2 = [100, 130, 375]
list3 = ['5.1%', '10.45%', '7.54%']
bonus = {name: sal * float(bon.strip("%")) / 100 for name, sal, bon in zip(list1, list2, list3)}
print(bonus)

# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonachi_gen(n):
    num1 = 0
    num2 = 1
    for i in range(1, n + 1):
        num2 += num1
        yield num1
        num1 = num2 - num1


for num in fibonachi_gen(10):
    print(f'{num}', end=" ")
