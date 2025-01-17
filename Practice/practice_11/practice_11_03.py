# Задача 3: Таблица умножения
"""
Напишите программу, которая запрашивает у пользователя число X
и выводит таблицу умножения для этого числа от 1 до 10 с помощью цикла while.
"""
def multiplication_table():
    # Запрос числа у пользователя
    x = int(input("Введите число X: "))

    # Инициализация переменной для счётчика
    multiplier = 1

    # Цикл while для вывода таблицы умножения
    while multiplier <= 10:
        result = x * multiplier
        print(f"{x} x {multiplier} = {result}")
        multiplier += 1  # Увеличиваем счётчик

# Вызов функции
multiplication_table()
