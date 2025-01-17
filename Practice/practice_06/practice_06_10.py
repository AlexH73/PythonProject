# Задание 10: Форматированное сообщение
"""
Создайте метод, который принимает имя пользователя и сообщение.
Метод должен вернуть строку вида: "[Имя]: [Сообщение]".
"""
def format_message(name, message):
    """
    Форматирует сообщение с именем пользователя.

    Аргументы:
    name (str): Имя пользователя.
    message (str): Сообщение пользователя.

    Возвращает:
    str: Форматированное сообщение.
    """
    return f"{name}: {message}"

# Пример использования метода
formatted_message = format_message("Владислав", "Привет всем!")
print(formatted_message)
