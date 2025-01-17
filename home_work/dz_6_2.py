# 2. Калькулятор площади круга:
"""
Напишите метод calculate_circle_area, который принимает радиус круга в качестве аргумента.
Метод должен рассчитать и вернуть площадь круга.
Формула: Площадь = π * радиус^2. Используйте 3.14 вместо π.
"""
# Определение функции.
def calculate_circle_area(radius):
    """
    Рассчитывает площадь круга.

    Аргументы:
    radius (float): Радиус круга.

    Возвращает:
    float: Площадь круга.
    """
    pi = 3.14
    return pi * (radius ** 2)

# Вызов и проверка метода
area = calculate_circle_area(5.6)
print(f"Площадь круга: {area:.2f}")
