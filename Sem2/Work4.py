import math
import decimal

# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. 
# Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.


decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

diameter = decimal.Decimal(input('Введите диаметр: '))

length = PI * diameter
square = PI * (diameter / 2) ** 2

print(f'{length = }')
print(f'{square = }')
