# # # # литеральные представления строк

text = 'привет, hello, ☺️'
text_2 = "привет, hello, ☺️"
text_3 = """привет, hello, ☺️"""
text_4 = '''привет, hello, ☺️'''

print(text)
print(text_2)
print(text_3)
print(text_4)

print(text == text_2 == text_3 == text_4)

# # # # ---

# # # # многострочные строки

text = 'Hello World\nMy name is Karl'
print(text)

text_2 = '''Hello World
My name is Karl
alkslkas
akslaks
asallsa
'''
print(text_2)

# # # # ---

# # # конкатенация строк

s1 = 'abc'
s2 = 'def'
s3 = 'Karl'

s4 = s1 + s2 + s3

print(
    s1 + s2 + s3 + s3 + s3 + 
    s3 + s3 + s3 + s3 + s3 + s3
)

# # # повторение строк

word_1 = 'Hello' * 5
word_2 = ' World'

print(word_1 + word_2 * 3)

text = 'Hello ' * 5

# индексы и срезы

s = 'Hello'

print(s[2])
print(s[1:3])
print(s[1:-2])

# # всякая всячина по строкам

s = 'cats are cool'

print(f"{len(s) = }")  # длина строки
print(f"{s.title() = }")  # первый символ всех слов в верхний регистр
print(f"{s.capitalize() = }")  # первый символ первого слова в верхний регистр
print(f"{s.upper() = }")  # все символы в верхний регистр
print(f"{s.lower() = }")  # все символы в нижний регистр
print(f"{s.replace('cats', 'cars') = }")  # подмена подстроки на подстроку
print(f"{s.strip() = }")  # удалить пробелы в начале и в конце строки

print(
    s.strip()
     .replace('cats', 'cars')
     .capitalize()
)

words = s.split(' ')
print(words)

s2 = ','.join(words)
print(s2)

s3 = s.replace(' ', '\n')
print(s3)


# # f-strings 

# # вывести по шаблону "hello, my name is ВАШЕ_ИМЯ!"

name = 'Karl'

print("hello, my name is " + name + "!")

print("hello, my name is %s!" % name)

print("hello, my name is {}!".format(name))

print(f"hello, my name is {name}!")

print(f"{len(name) = }")

s = f"wowowowoowow { 1 + 2 = } wowowowoowow"
print(s)

# Специальные символы
# Символ 	Описание
# \n 	Перенос строки
# \t 	Горизонтальная табуляция
# \' 	Одинарная кавычка
# \" 	Двойная кавычка
# \\ 	Обратный слэш

s = '\'karl\''
print(s)

s = 'karl'
print(s)

s = '\tHello world!\n\tMy name is Karl'
print(s)
