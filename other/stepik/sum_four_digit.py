def sum_four_digit_numbers_with_digit_sum(target_sum):
    """
    Находит сумму всех четырехзначных чисел, сумма цифр которых равна заданному значению.

    Args:
        target_sum: Целое число, представляющее сумму цифр.

    Returns:
        Сумма четырехзначных чисел с заданной суммой цифр.
    """
    total_sum = 0  # Инициализируем общую сумму
    for number in range(1000, 10000): # Перебираем все 4-значные числа
        number_str = str(number) # Преобразовываем число в строку
        digit_sum = 0 # Инициализируем сумму цифр
        for digit in number_str: # Перебираем цифры в числе
            digit_sum += int(digit) # Добавляем число к сумме цифр
        if digit_sum == target_sum:  # Проверяем, равна ли сумма цифр нужной сумме
            total_sum += number # Если равна, то добавляем число к сумме всех чисел
    return total_sum # Возвращаем сумму

# Указываем сумму цифр
target_sum = 20

# Вызываем функцию и выводим результат
result = sum_four_digit_numbers_with_digit_sum(target_sum)
print(result)