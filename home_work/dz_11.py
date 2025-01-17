# Задача 1: Чётные числа в диапазоне
"""
Напишите программу, которая принимает от пользователя два числа: start и end.
С помощью цикла while выведите все чётные числа в диапазоне от start до end (включительно).
Если start больше end, выведите сообщение: "Неверный диапазон."
"""
def print_even_numbers(start, end):
    if start > end:
        print("Неверный диапазон.")
    else:
        while start <= end:
            if start % 2 == 0:
                print(start)
            start += 1

# Запрашиваем у пользователя ввод чисел start и end
start = int(input("Введите начальное число (start): "))
end = int(input("Введите конечное число (end): "))

# Вызываем функцию для вывода чётных чисел
print_even_numbers(start, end)

# Задача 2: Вычисление факториала
"""
Напишите программу, которая принимает от пользователя число N и вычисляет его факториал
с использованием цикла while. Факториал числа — это произведение всех положительных
целых чисел, меньших или равных этому числу. Например, факториал числа 5 равен
5 × 4 × 3 × 2 × 1 = 120.
"""
def calculate_factorial(N):
    factorial = 1
    i = 1
    while i <= N:
        factorial = factorial * i
        i = i + 1
    return factorial

# Запрашиваем у пользователя ввод числа N
n = int(input("Введите число N: "))

# Вычисляем факториал и выводим результат
result = calculate_factorial(n)
print(f"Факториал числа {n} равен {result}")

# Задача 3: Обращение числа
"""
Напишите программу, которая принимает от пользователя положительное целое число
и переворачивает его цифры с использованием цикла while. Например, если пользователь
вводит 1234, программа должна вывести 4321.
"""
def reverse_number():
    while True:
        # Запрашиваем у пользователя ввод положительного целого числа
        number = int(input("Введите положительное целое число: "))

        # Проверяем, является ли число отрицательным
        if number < 0:
            print("Вы ввели отрицательное число. Попробуйте снова.")
            continue

        # Инициализируем переменную для хранения перевёрнутого числа
        reversed_number = 0

        # Используем цикл while для переворачивания цифр числа
        while number > 0:
            # Получаем последнюю цифру числа
            digit = number % 10

            # Добавляем цифру к перевёрнутому числу
            reversed_number = reversed_number * 10 + digit

            # Убираем последнюю цифру из исходного числа
            number = number // 10

        # Выводим перевёрнутое число
        print(f"Перевёрнутое число: {reversed_number}")
        break

# Вызываем функцию для переворачивания числа
reverse_number()

# Задача 4: Сумма цифр
"""
Напишите программу, которая принимает от пользователя положительное целое число
и вычисляет сумму его цифр с использованием цикла while. Например, если пользователь
вводит 123, программа должна вывести 6 (1 + 2 + 3).
"""
def sum_of_digits():
    while True:
        # Запрашиваем у пользователя ввод положительного целого числа
        number = int(input("Введите положительное целое число: "))

        # Проверяем, является ли число отрицательным
        if number < 0:
            print("Вы ввели отрицательное число. Попробуйте снова.")
            continue

        # Инициализируем переменную для хранения суммы цифр
        sum_digits = 0

        # Используем цикл while для вычисления суммы цифр
        while number > 0:
            # Получаем последнюю цифру числа
            digit = number % 10

            # Добавляем цифру к сумме
            sum_digits += digit

            # Убираем последнюю цифру из числа
            number = number // 10

        # Выводим сумму цифр
        print(f"Сумма цифр числа равна {sum_digits}")
        break

# Вызываем функцию для вычисления суммы цифр
sum_of_digits()