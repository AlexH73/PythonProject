# 3. Приветствие с титулом:
"""
Напишите метод greet_with_title, который принимает титул (например, "доктор") и имя.
Метод должен вернуть строку: "Привет, [Титул] [Имя]!".
"""
# Определение функции.
def greet_with_title(title, name):
    """
    Возвращает приветственное сообщение с титулом и именем.

    Аргументы:
    title (str): Титул (например, "доктор").
    name (str): Имя пользователя.

    Возвращает:
    str: Приветственное сообщение.
    """
    return f"Привет, {title} {name}!"

# Вызов и проверка метода
greeting = greet_with_title("доктор", "Иванов")
print(greeting)
