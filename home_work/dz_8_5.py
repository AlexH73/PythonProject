# 5. Строка содержит цифру:
"""
Напишите метод contains_digit, который принимает строку.
Метод должен возвращать True, если строка содержит хотя бы одну цифру.
Иначе метод должен возвращать False.
"""
# Определение функции
def contains_digit(line):
    # Проверка наличия цифры и возврат результата
    """
    Тут не большая загвоздка, лично мне нравится решение следующей строки,
    но не знаю на сколько это соответствует нашим текущим скилам.
    Поэтому я ее закомментирую и ниже добавлю еще одну строку решения,
    она конечно очень топорная, но тоже работает.
    Другого ничего к сожалению не придумал. Если есть какое-то более аккуратное решение,
    прошу мне его написать. Спасибо.
    """
    #return any(char.isdigit() for char in line)
    return( '0' in line or '1' in line or
            '2' in line or '3' in line or
            '4' in line or '5' in line or
            '6' in line or '7' in line or
            '8' in line or '9' in line
            )

# Ввод данных
s = input("Введите строку: ")

# Вызов метода и вывод результата
print(contains_digit(s))