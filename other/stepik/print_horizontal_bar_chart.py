def print_horizontal_bar_chart(numbers):
    """
    Выводит горизонтальную столбчатую диаграмму из заданных чисел.

    Args:
        numbers: Список натуральных чисел.
    """
    for num in numbers:  # Перебираем все числа
        print("*" * num) # Выводим строку из звездочек, длиной равной значению числа


# Получаем ввод от пользователя
try:
  input_str = input("Введите натуральные числа, разделенные пробелами: ")
  numbers = list(map(int, input_str.split()))

  if any(num <= 0 for num in numbers):
      print("Ошибка: Введены не натуральные числа.")
  else:
     print_horizontal_bar_chart(numbers)  # Вызываем функцию для вывода диаграммы

except ValueError:
     print("Ошибка: Некорректный ввод. Пожалуйста, введите натуральные числа, разделенные пробелами.")
