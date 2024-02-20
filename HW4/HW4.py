# Напишите функцию для транспонирования матрицы


def matrix_transpose(m):
    new = []
    for i in range(len(m[0])):
        new.append([])
    for i in range(len(m)):
        for j in range(len(m[i])):
            new[j].append(m[i][j])
    return new
    
    
print(matrix_transpose([[1, 2], [3, 4], [5, 6]]))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую 
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def make_dict_keys(**kwargs):
    d = {}
    for key, value in kwargs.items():
        try:
            d[value] = key
        except:
            value = str(value)
            d[value] = key
    return d
    
    
print(make_dict_keys(a=5, b=6, c=[8, 9]))


# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def main():
    balance = 0
    count = 0
    global operation
    operation = []
    print('Добро пожаловать в банкомат!')
    while True:
        while True:
            # print(operation)
            act = input(
                'Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - выйти\n')
            if act not in ("1", "2", "3"):
                print("Неверный ввод")
            else:
                break
        match act:
            case "1":
                balance, count = add_money(balance, count)
                print(f"Ваш баланс {balance}")
            case "2":
                balance, count = get_money(balance, count)
                print(f"Ваш баланс {balance}")
            case "3":
                print(f"Ваш баланс {balance}")
                print("До свидания!")
                break


def add_money(balance, count):
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    operation.append(f"Пополнение на {summ}")
    return balance, count


def get_money(balance, count):
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
        if perc < 30:
            perc = 30
        elif perc > 600:
            perc = 600
        if summ + perc > balance:
            print("Недостаточно средств!")
            continue
        else:
            break
    balance -= (summ + perc)
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    operation.append(f"Снятие на {summ}")
    return balance, count


if __name__ == "__main__":
    main()
