# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

def sort(my_list: list) -> list:
    for _ in range(len(my_list)):
        for j in range(1, len(my_list)):
            if my_list[j - 1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j -1]
    return my_list


some_list = [1455, 3434, 1066, 2334, 4343, 565]
print(sort(some_list))


if __name__ == '__main__':
    some_list = [1103, 1102, 1096, 1094, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085]
    print(some_list)
    print(sort(some_list))