# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт» без перехода на новую строку.

my_table = (f'{j} * {i} = {j * i}\t' if j < 5 else f'{j} * {i} = {j * i}\n'
            for i in range(2, 11) for j in range(2, 6))
for i in my_table:
    print(i, end='')
print()
my_table = (f'{j} * {i} = {j * i}\t' if j < 9 else f'{j} * {i} = {j * i}\n'
            for i in range(2, 11) for j in range(6, 10))
for i in my_table:
    print(i, end='')
