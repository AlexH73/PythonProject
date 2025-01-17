# Задание 8: Форматированное описание
"""
Создайте метод, который принимает название фильма, режиссёра и год выхода.
Метод должен вернуть строку вида: "[Название фильма]" снят режиссёром [Режиссёр] в [Год].
"""
def movie_info(title, director, year):
    """
    Возвращает информацию о фильме.

    Аргументы:
    title (str): Название фильма.
    director (str): Режиссёр фильма.
    year (int): Год выхода фильма.

    Возвращает:
    str: Сообщение о фильме.
    """
    return f'"{title}" снят режиссёром {director} в {year}.'

# Пример использования метода
info = movie_info("Интерстеллар", "Кристофер Нолан", 2014)
print(info)
