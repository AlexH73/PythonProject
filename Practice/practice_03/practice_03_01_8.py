# Задание 8: Частотный анализ
"""
Создайте строку с текстом "Python Python Python Java Java C++".
- Разбейте строку на отдельные слова.
- Подсчитайте, сколько раз каждое слово встречается в строке.
- Выведите результаты.
"""
# Создаем строку
text = "Python Python Python Java Java C++"

# Разбиваем строку на отдельные слова
words = text.split()

# Подсчитываем, сколько раз каждое слово встречается в строке
word_count = dict(map(lambda word: (word, words.count(word)), set(words)))

# Выводим результаты
print(word_count)
