# Задание 6: Преобразование в список
"""
Создайте метод split_sentence(sentence), который принимает строку с несколькими словами, разделёнными пробелами.
Метод должен вернуть список слов, полученных из этой строки.
Пример: для строки "Привет мир" метод должен вернуть ["Привет", "мир"].
"""
# Назначаем функцию
def split_sentence(sentence):
    # Обработка и возврат
    return sentence.split()
# Вызов и вывод
print(split_sentence("Привет мир"))