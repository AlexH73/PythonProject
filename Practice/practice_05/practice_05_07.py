# Задание 7: Расчёт среднего арифметического
"""
Запросите у пользователя три числа.
Рассчитайте и выведите их среднее арифметическое с точностью до двух знаков после запятой.
"""
#  Запрашиваем ввод чисел
numberOne = float(input("Введите первое число:"))
numberTwo = float(input("Введите второе число:"))
numberThree = float(input("Введите третье число:"))

# Арифметика.
average = (numberOne + numberTwo + numberThree) / 3

# Вывод.
print("Среднее арифметическое число = %2.f" % (average))