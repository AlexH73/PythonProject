# Задача 6: Проверка температуры
"""
Напишите метод temperature_status(temp), который принимает температуру.
Метод должен вернуть:
- "Холодно", если температура ниже 10.
- "Прохладно", если от 10 до 20.
- "Тепло", если от 21 до 30.
- "Жарко", если больше 30.
"""
# Назначаем функцию
def temperature_status(temp):
    # Определяем статус температуры на основе значения
    if temp < 10:
        return "Холодно"
    elif 10 <= temp <= 20:
        return "Прохладно"
    elif 21 <= temp <= 30:
        return "Тепло"
    else:
        return "Жарко"

# Вызов и вывод
print(temperature_status(5))   # Холодно
print(temperature_status(15))  # Прохладно
print(temperature_status(25))  # Тепло
print(temperature_status(35))  # Жарко
