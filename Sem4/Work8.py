# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся 
# на s (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def func() -> None:
    g = globals()
    change = {}
    for key, value in g.items():
        if key == 's':
            continue
        if key.endswith('s'):
            change[key[:-1]] = g[key]
            g[key] = None
    for key, value in change.items():
        g[key] = value
                
                
datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

func()
print(globals())
