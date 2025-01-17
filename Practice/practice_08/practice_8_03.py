# Задание 3: Проверка содержания
"""
Создайте метод contains_substring(string, substring), который принимает строку и подстроку.
Метод должен возвращать True, если подстрока содержится в строке.
Иначе метод должен возвращать False.
"""
# Назначаем функцию
def contains_substring(string, substring):
    # Проверяем, содержится ли подстрока в строке
    return substring in string

# Вызов и вывод
print(contains_substring("Привет, мир!", "мир"))
