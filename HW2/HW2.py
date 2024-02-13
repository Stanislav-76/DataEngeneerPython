# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

from fractions import Fraction
HEX = 16

num: int = int(input('Введите число: '))
test_num: int = num
result: str = ''
while test_num > 0:
    numHex = test_num % HEX
    if numHex < 10:
        result = str(numHex) + result
    else:
        result = chr(97 + numHex - 10) + result
        # result = "abcdef"[numHex - 10] + result
    test_num //= HEX
print(f'For {HEX} {result =}')
print(f'{hex(num)   =}')

# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение дробей. Для проверки
# своего кода используйте модуль fractions.


def sum_fract(a1, b1, a2, b2):
    chisl = a1 * b2 + a2 * b1
    znam = b1 * b2
    for i in range(2, int(znam**0.5)):
        while chisl % i == znam % i == 0:
            chisl //= i
            znam //= i
    return f'{chisl}/{znam}'


def mult_fract(a1, b1, a2, b2):
    chisl = a1 * a2
    znam = b1 * b2
    for i in range(2, int(znam**0.5)):
        while chisl % i == znam % i == 0:
            chisl //= i
            znam //= i
    return f'{chisl}/{znam}'


a1, b1 = [int(i) for i in input("Введите первую дробь через/ ").split("/")]
a2, b2 = [int(i) for i in input("Введите вторую дробь через/ ").split("/")]
s = sum_fract(a1, b1, a2, b2)
p = mult_fract(a1, b1, a2, b2)
a = Fraction(a1, b1)
b = Fraction(a2, b2)
print(f"{s} = {a + b}, {p} = {a * b}")
