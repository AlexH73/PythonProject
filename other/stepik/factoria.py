def factorial(n):
    """
    Вычисляет факториал целого числа n.

    Args:
      n: Целое число (n >= 0).

    Returns:
      Факториал числа n.
    """
    if n == 0 or n == 1: # Обработка крайних случаев 0! и 1!
        return 1
    factorial = 1 # Инициализируем факториал
    for i in range(2, n + 1):  # Перебираем числа от 2 до n
      factorial *= i # Умножаем факториал на i
    return factorial # Возвращаем факториал

# Получаем ввод от пользователя:
number = int(input("Введите целое число n (n >= 0): "))

# Вызываем функцию и выводим результат:
result = factorial(number)
print(f"Факториал числа {number}: {result}")