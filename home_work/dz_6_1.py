# 1. Калькулятор периметра квадрата:
"""
Напишите метод calculate_perimeter, который принимает длину стороны квадрата в качестве аргумента.
Метод должен рассчитать и вернуть периметр квадрата.
Формула: Периметр = 4 * длина стороны.
"""
# Определение функции.
def calculate_perimeter(side_length):
    """
    Рассчитывает периметр квадрата.

    Аргументы:
    side_length (float): Длина стороны квадрата.

    Возвращает:
    float: Периметр квадрата.
    """
    return 4 * side_length

# Вызов и проверка метода
perimeter = calculate_perimeter(5.79)
print(f"Периметр квадрата: {perimeter:.2f}")
