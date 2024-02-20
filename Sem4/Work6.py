# Функция получает на вход список чисел и два индекса. 
# Вернуть сумму чисел между переданными индексами. 
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_numbers(numbers: list, start: int, stop: int) -> int:
    if start > stop:
        stop, start = start, stop
    if start < 0:
        start = 0
    if stop > len(numbers) - 1:
        stop = len(numbers) - 1
    return sum(numbers[start: stop + 1])


if __name__ == "__main__":
    my_list = [43, 3454, 3, 355, 35, 65, 434, 42, 123, 66, 6]
    print(sum_numbers(my_list, 5, 1))
    