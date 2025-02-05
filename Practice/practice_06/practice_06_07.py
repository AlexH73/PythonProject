# Задание 7: Среднее арифметическое
"""
Создайте метод, который принимает три числа.
Метод должен рассчитать и вернуть их среднее арифметическое.
"""
def calculate_average(a, b, c):
    """
    Рассчитывает среднее арифметическое трех чисел.

    Аргументы:
    a (float): Первое число.
    b (float): Второе число.
    c (float): Третье число.

    Возвращает:
    float: Среднее арифметическое трех чисел.
    """
    return (a + b + c) / 3

# Пример использования метода
average = calculate_average(4.2, 8.7, 12)
print(f"Среднее арифметическое: {average:.2f}")
