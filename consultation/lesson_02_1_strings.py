# Конкатенация строк.

s1 = "abc"
s2 = "def"
s3 = "Karl"
s4 = s2 + s1 +s3

print(s4)

# Повторение строк.

word_1 = "Hello "
word_2 = "World "

print(word_2 * 3 + word_1)

# Индексы

s = "Hello"

print(s[0])
print(s[-3])
print(s[0:-3])

# Всякая всячина по срокам.
s = "cat are cool"

print(len(s))
print(s.title())
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('t', 'rs'))

print(f"{len(s) = }")  # длина строки
print(f"{s.title() = }")  # первый символ всех слов в верхний регистр
print(f"{s.capitalize() = }")  # первый символ первого слова в верхний регистр
print(f"{s.upper() = }")  # все символы в верхний регистр
print(f"{s.lower() = }")  # все символы в нижний регистр
print(f"{s.replace('cats', 'cars') = }")  # подмена подстроки на подстроку
print(f"{s.strip() = }")  # удалить пробелы в начале и в конце строки
