# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def ch_to_list(text: str):
    return sorted(set([ord(symbol) for symbol in text]), reverse=True)


text = "Экземпляр списка является компьютерной реализацией математического понятия конечной последовательности."
print(ch_to_list(text))
