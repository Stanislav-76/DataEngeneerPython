from random import randint

def guess(lower_limit: int = 0, upper_limit: int = 1000, attempt_number: int = 10):
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
            