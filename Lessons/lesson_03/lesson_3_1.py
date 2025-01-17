text = "Python "

print(text * 3)  # Вывод: Python Python Python

name = "Ильяс"

greeting = "Привет, " + name + "!"

print(greeting)  # Вывод: Привет, Ильяс!

name = "Ильяс"

greeting = "Привет, " + name + "!"

print(greeting)  # Вывод: Привет, Ильяс!

word = "Python"  # ['P', 'y', 't', 'h', 'o', 'n']
                 # [ 0,   1,   2,   3,   4,   5 ]


print(word[2])

print(word[5])

startIndex = 4

endIndex = 6

file = "code.py"

print(file[startIndex:endIndex])  # подобная конструкция называется "срез" или подстрока.
# Что это такое? Это часть строки начиная с символа, находящегося под индексом startIndex
# и заканчивая индексом endIndex, но не включая символ под индексом endIndex
# поэтому, если мы хотим увидеть строку, начиная от какого-то индекса, до конца, то мы можем использовать следующее:

print(file[startIndex:])

## "./AAPL" "^AMZN"
# для того, чтобы получить количество сим волов в строке, можно воспользоваться встроенной функцией языка Python - len(str)


path = "/lesson_03/code/teachers_code_1.py"

path_len = len(path)

print(path_len)

# всегда будем получать последний символ

print(path[path_len - 1])

# получить расширение файла

print(path[(path_len - 3):])