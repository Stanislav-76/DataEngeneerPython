# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.


from module2 import guess_riddle
from Work5 import list_riddles
# __all__ = ['start']


_dict_riddles = {}

def guess1(rid: str, num_attemp: int):
    if rid not in _dict_riddles:
        _dict_riddles[rid] = [num_attemp]
    else:
        _dict_riddles[rid].append(num_attemp)


def riddle_result():
    for v in _dict_riddles.values():
        print(f'результат угадывания {v}')


def start():
    for i, j in list_riddles():
        guess1(i, j)
    riddle_result()


if __name__ == '__main__':
    start()