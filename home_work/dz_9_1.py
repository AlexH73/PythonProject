"""
Диапазон температуры:
Напишите метод is_in_temperature_range, который принимает температуру и два предела (min и max) в качестве аргументов.
Метод должен возвращать True, если температура находится в диапазоне [min, max].
Иначе метод должен возвращать False.
"""
# Назначаем метод и аргументы
def is_in_temperature_range(temp, min_temp, max_temp):
    # Проверка условий и возврат
    return min_temp <= temp <= max_temp

# Запуск и вывод результата
print(is_in_temperature_range(30, 17, 35))
