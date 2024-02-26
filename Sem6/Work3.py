# Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from sys import argv
from random import randint

def guess(lower_limit: int, upper_limit: int, attempt_number: int):
    # lower_limit = 0
    # upper_limit = 1000
    # attempt_number = 10
    num = randint(lower_limit, upper_limit)
    count = 0
    while True:
        count += 1
        my_attemp = int(input('Введите вариант загаданного числа => '))
        if my_attemp == num:
        # print(f'Вы угадали, загаданное число, действительно {my_attemp}.')
            return True
        elif count == attempt_number:
        # print(f'К сожалению, это была последняя {attempt_number} попытка.')
            return False
        elif my_attemp < num:
            print(f'{my_attemp} - не угадали, попробуйте число побольше.')
        elif my_attemp > num:
            print(f'{my_attemp} - не угадали, попробуйте число поменьше.')


if __name__=="__main__":
    args = [int(i) for i in argv[1:]]
    if len(args) < 1:
        print("Not enough arguments")
    if len(args) in (1, 2, 3):
        lower_limit = args[0]
    if len(args) in (2, 3):
        upper_limit = args[1]
    if len(args) == 3:
        attempt_number = args[2]
    print(guess(lower_limit, upper_limit, attempt_number))