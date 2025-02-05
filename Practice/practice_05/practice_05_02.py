# Задание 2: Преобразование температуры
"""
Запросите у пользователя температуру в градусах Цельсия.
Преобразуйте её в градусы Фаренгейта по формуле F = C * 9/5 + 32.
Выведите результат с точностью до двух знаков после запятой.
"""
# Запрашиваем вводные данные и назначаем переменную.
degreeCelsius = float(input("Введите температуру в градусах по цельсию:"))

# Высчитываем Фаренгейта.
degreesFahrenheit = degreeCelsius * 9/5 + 32

# Формируем и выводим строку.
print(f"{degreeCelsius:.2f} ℃ равно {degreesFahrenheit:.2f} ℉.")