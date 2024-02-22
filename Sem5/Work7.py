# Создайте функцию-генератор. 
# Функция генерирует N простых чисел, начиная с числа 2. 
# Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».

def check_num(num: int) -> bool:
    flag = False
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+2, 2):
            if num % i == 0:
                return False
            else:
                flag = True
    return flag

def gen_nums(n: int):
    count = 0
    i = 2
    while count < n:
        if check_num(i):
            count += 1
            yield i
        i += 1

for i in gen_nums(10):
    print(i, end=' ')