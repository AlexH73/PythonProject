# Задача 6: Обратный отсчёт
"""
Напишите программу, которая выводит обратный отсчёт от 10 до 1, используя цикл while.
По завершении отсчёта программа выводит сообщение: "Время вышло!"
"""
def countdown():
    # Инициализация счётчика
    number = 10

    # Обратный отсчёт с помощью цикла while
    while number > 0:
        print(number)
        number -= 1  # Уменьшаем значение счётчика на 1

    # Вывод сообщения после завершения отсчёта
    print("Время вышло!")

# Вызов функции
countdown()
