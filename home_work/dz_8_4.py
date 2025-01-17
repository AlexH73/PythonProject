# 4. Сравнение длины строк:
"""
Напишите метод is_longer_than, который принимает две строки.
Метод должен возвращать True, если первая строка длиннее второй.
Иначе метод должен возвращать False.
"""
# Определение функции
def is_longer_than(str_1, str_2):
    # Сравнение количества символов и возврат результата
    return len(str_1) > len(str_2)

# Ввод данных
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

# Вызов метода и вывод результата
print(is_longer_than(str1, str2))
