textWithSpaces = "    some text with spaces   "

print("*" + textWithSpaces + "*")

# удаляем пробелы в начале и в конце строки
textWithSpaces = textWithSpaces.strip()
print("*" + textWithSpaces + "*")
textWithSpaces = """    

some text with spaces



   """

print("*" + textWithSpaces + "*")

# вне зависимости, что это за пробелы - пустая строка или пробел, он будет удален
textWithSpaces = textWithSpaces.strip()
print("*" + textWithSpaces + "*")