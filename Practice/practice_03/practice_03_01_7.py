# Задание 7: Работа со списком слов
"""
Создайте строку с текстом "учеба, кодинг, отдых, прогулка".
- Разбейте строку на слова.
- Сделайте каждое слово заглавным (с большой буквы).
- Объедините слова обратно в строку, разделяя их запятыми.
"""
# Создаем строку
text = "учеба, кодинг, отдых, прогулка"

# Разбиваем строку на слова
words = text.split(", ")

# Делаем каждое слово заглавным
capitalized_words = [word.capitalize() for word in words]

# Объединяем слова обратно в строку, разделяя их запятыми
result = ", ".join(capitalized_words)

# Выводим результат
print(result)
