# Задание 1: Преобразование регистра
"""
Создайте строку с текстом "Python Programming IS Awesome!".
Выполните следующие операции:
- Преобразуйте строку в нижний регистр.
- Преобразуйте строку в верхний регистр.
- Сделайте первую букву строки заглавной.
"""
# Создаем строку
text = "Python Programming IS Awesome!"

# Преобразуем строку в нижний регистр
lowercase_text = text.lower()
print("Нижний регистр:", lowercase_text)

# Преобразуем строку в верхний регистр
uppercase_text = text.upper()
print("Верхний регистр:", uppercase_text)

# Делаем первую букву строки заглавной
capitalized_text = text.capitalize()
print("Первая буква заглавная:", capitalized_text)
