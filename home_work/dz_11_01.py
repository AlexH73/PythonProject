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
