# 3. Проверка чётности и положительности:
"""
Напишите метод is_even_and_positive, который принимает число.
Метод должен возвращать True, если число чётное и положительное.
Иначе метод должен возвращать False.
"""
# Назначаем метод и аргумент
def is_even_and_positive(num):
    # Проверка условий и возврат
    if num % 2 == 0 and num > 0:
        return True
    else:
        return False

# Запуск и вывод результата
print(is_even_and_positive(10))