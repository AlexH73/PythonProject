# Задание 4: Разделение строки
"""
Создайте строку с текстом "яблоко,банан,вишня".
- Разбейте её на отдельные слова, используя запятую как разделитель.
- Выведите полученный список.
"""
# Создаем строку
text = "яблоко,банан,вишня"

# Разбиваем строку на отдельные слова, используя запятую как разделитель
words = text.split(",")

# Выводим полученный список
print(words)
