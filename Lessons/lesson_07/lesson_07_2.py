# Задание 2: Соединение слов
"""
Создайте метод join_words(word1, word2), который принимает два слова в виде строк.
Метод должен вернуть строку, где два слова объединены через пробел.
Пример: для слов "Привет" и "мир" метод должен вернуть "Привет мир".
"""
# Назначаем функцию
def join_words(word1, word2):
    # Выполнение логики
    words = [word1, word2]
    joinWords = " " .join(words)
    # Возврат
    return joinWords
# Вызов и вывод
print(join_words("Привет", "мир"))