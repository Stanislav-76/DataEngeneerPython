# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 2, 73, 42]

result = []
for item in set(data):
    if data.count(item) > 1:
        result.append(item)

print(f'{result = }')


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

text = """В информатике, список (англ. list) — это абстрактный тип данных, представляющий 
собой упорядоченный набор значений, в котором некоторое значение может 
встречаться более одного раза. Экземпляр списка является компьютерной 
реализацией математического понятия конечной последовательности. Экземпляры 
значений, находящихся в списке, называются элементами списка (англ. item, entry 
либо element); если значение встречается несколько раз, каждое вхождение 
считается отдельным элементом."""

for alpfa in text:
    if not alpfa.isalpha() and alpfa != " ":
        text = text.replace(alpfa, "")

words = text.lower().split()
result = {}
for word in set(words):
    result[word] = words.count(word)
count = 0
for i in list(set(result.values()))[::-1]:
    for key, value in result.items():
        if count == 10:
            break
        if value == i:
            print(f"{count + 1} {key}: {value}")
            count += 1


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

hike = {"спички": 0.1, "ложка": 0.2, "нож": 0.3, "спальник": 2,
        "канистра": 2, "топор": 5, "вода": 4, "еда": 3}
weight = int(input("Введите максимальный вес рюкзака, кг: "))
result = []
total_weght = weight
for key, value in hike.items():
    if total_weght > value:
        result.append(key)
        total_weght -= value

print(result)
print()


# Все варианты с наполнением максимального веса (нет вещей которые можно добавить)

variant = 2**len(hike) - 1
result_new = []
hike_list = list(hike)

while variant > 0:
    total_weght = weight
    result_do = []
    for i in range(2, len(bin(variant))):
        pos = int(bin(variant)[i])
        weigt_pos = hike.get(hike_list[i - 2])
        if pos:
            result_do.append(hike_list[i - 2])
            total_weght -= weigt_pos
        if total_weght < 0:
            break

    if total_weght >= 0:
        flag = True
        for key, value in hike.items():
            if value < total_weght and key not in result_do:
                flag = False
                break
        if flag and result_do not in result_new:
            result_new.append(result_do)
            result_new.append(weight - total_weght)
    variant -= 1

print(result_new)
