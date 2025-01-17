# 2. Проверка порядка строк:
"""
Напишите метод is_substring_first, который принимает две строки.
Метод должен возвращать True, если первая строка находится раньше второй в алфавитном порядке.
Иначе метод должен возвращать False.
"""
# Определяем функцию
def is_substring_first(first_line, second_line):
    # Сравнение двух строк и возврат результата
    return first_line < second_line

# Ввод данных
firstLine = input("Введите первую строку: ")
secondLine = input("Введите вторую вторую: ")

# Вызов метода и вывод результата
print(is_substring_first(firstLine, secondLine))