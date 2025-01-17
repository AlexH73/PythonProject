# 1. capitalize() - Преобразует первый символ строки в верхний регистр.
text = "hello world"
print(f"1. {text.capitalize() = }")  # "Hello world"

# 2. casefold() - Преобразует строку в нижний регистр.
text = "HELLO WORLD"
print(f"2. {text.casefold() = }")  # "hello world"

# 3. center(width, fillchar) - Центрирует строку, используя символ fillchar (по умолчанию пробел).
text = "hello"
print(f"3. {text.center(10, '-') = }")  # "--hello---"

# 4. count(sub, start, end) - Возвращает количество непересекающихся вхождений подстроки sub в строке.
text = "hello world"
print(f"4. {text.count('o') = }")  # 2

# 5. encode(encoding, errors) - Кодирует строку в байты, используя указанный кодек.
text = "hello"
print(f"5. {text.encode('utf-8') = }")  # b'hello'

# 6. endswith(suffix, start, end) - Проверяет, заканчивается ли строка указанным суффиксом.
text = "hello world"
print(f"6. {text.endswith('world') = }")  # True

# 7. expandtabs(tabsize) - Заменяет символы табуляции пробелами.
text = "hello\tworld"
print(f"7. {text.expandtabs(4) = }")  # "hello   world"

# 8. find(sub, start, end) - Возвращает наименьший индекс в строке, где подстрока sub найдена.
text = "hello world"
print(f"8. {text.find('world') = }")  # 6

# 9. format(*args, **kwargs) - Форматирует строку, используя переданные аргументы.
text = "Hello, {}!"
print(f"9. {text.format('world') = }")  # "Hello, world!"

# 10. format_map(mapping) - Форматирует строку, используя переданный словарь.
text = "Hello, {name}!"
print(f"10. {text.format_map({'name': 'world'}) = }")  # "Hello, world!"

# 11. index(sub, start, end) - Возвращает наименьший индекс в строке, где подстрока sub найдена (вызывает ValueError, если не найдена).
text = "hello world"
print(f"11. {text.index('world') = }")  # 6

# 12. isalnum() - Проверяет, состоит ли строка только из буквенно-цифровых символов.
text = "hello123"
print(f"12. {text.isalnum() = }")  # True

# 13. isalpha() - Проверяет, состоит ли строка только из букв.
text = "hello"
print(f"13. {text.isalpha() = }")  # True

# 14. isascii() - Проверяет, состоит ли строка только из ASCII символов.
text = "hello"
print(f"14. {text.isascii() = }")  # True

# 15. isdecimal() - Проверяет, состоит ли строка только из десятичных цифр.
text = "12345"
print(f"15. {text.isdecimal() = }")  # True

# 16. isdigit() - Проверяет, состоит ли строка только из цифр.
text = "12345"
print(f"16. {text.isdigit() = }")  # True

# 17. isidentifier() - Проверяет, является ли строка допустимым идентификатором.
text = "hello_world"
print(f"17. {text.isidentifier() = }")  # True

# 18. islower() - Проверяет, все ли символы строки в нижнем регистре.
text = "hello"
print(f"18. {text.islower() = }")  # True

# 19. isnumeric() - Проверяет, состоит ли строка только из числовых символов.
text = "12345"
print(f"19. {text.isnumeric() = }")  # True

# 20. isprintable() - Проверяет, все ли символы строки печатные.
text = "hello world"
print(f"20. {text.isprintable() = }")  # True

# 21. isspace() - Проверяет, состоит ли строка только из пробельных символов.
text = "   "
print(f"21. {text.isspace() = }")  # True

# 22. istitle() - Проверяет, является ли строка заголовком (каждое слово начинается с заглавной буквы).
text = "Hello World"
print(f"22. {text.istitle() = }")  # True

# 23. isupper() - Проверяет, все ли символы строки в верхнем регистре.
text = "HELLO"
print(f"23. {text.isupper() = }")  # True

# 24. join(iterable) - Объединяет элементы итерируемого объекта в строку, используя текущую строку как разделитель.
text = "-"
print(f"24. {text.join(['hello', 'world']) = }")  # "hello-world"

# 25. ljust(width, fillchar) - Выравнивает строку по левому краю, используя символ fillchar (по умолчанию пробел).
text = "hello"
print(f"25. {text.ljust(10, '-') = }")  # "hello-----"

# 26. lower() - Преобразует все символы строки в нижний регистр.
text = "HELLO"
print(f"26. {text.lower() = }")  # "hello"

# 27. lstrip(chars) - Удаляет начальные символы, указанные в chars (по умолчанию пробелы).
text = "   hello"
print(f"27. {text.lstrip() = }")  # "hello"

# 28. maketrans(x, y, z) - Возвращает таблицу преобразований для использования с методом translate().
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
text = "hello world"
print(f"28. {text.translate(trantab) = }")  # "h2ll4 w4rld"

# 29. partition(sep) - Разделяет строку на три части: до разделителя, сам разделитель и после разделителя.
text = "hello world"
print(f"29. {text.partition(' ') = }")  # ('hello', ' ', 'world')

# 30. replace(old, new, count) - Заменяет вхождения подстроки old на new.
text = "hello world"
print(f"30. {text.replace('world', 'Python') = }")  # "hello Python"

# 31. rfind(sub, start, end) - Возвращает наибольший индекс в строке, где подстрока sub найдена.
text = "hello world"
print(f"31. {text.rfind('o') = }")  # 7

# 32. rindex(sub, start, end) - Возвращает наибольший индекс в строке, где подстрока sub найдена (вызывает ValueError, если не найдена).
text = "hello world"
print(f"32. {text.rindex('o') = }")  # 7

# 33. rjust(width, fillchar) - Выравнивает строку по правому краю, используя символ fillchar (по умолчанию пробел).
text = "hello"
print(f"33. {text.rjust(10, '-') = }")  # "-----hello"

# 34. rpartition(sep) - Разделяет строку на три части, начиная с конца: до разделителя, сам разделитель и после разделителя.
text = "hello world"
print(f"34. {text.rpartition(' ') = }")  # ('hello', ' ', 'world')

# 35. rsplit(sep, maxsplit) - Разделяет строку на части, начиная с конца.
text = "hello world"
print(f"35. {text.rsplit(' ', 1) = }")  # ['hello', 'world']

# 36. rstrip(chars) - Удаляет конечные символы, указанные в chars (по умолчанию пробелы).
text = "hello   "
print(f"36. {text.rstrip() = }")  # "hello"

# 37. split(sep, maxsplit) - Разделяет строку на части.
text = "hello world"
print(f"37. {text.split() = }")  # ['hello', 'world']

# 38. splitlines(keepends) - Разделяет строку на части по символам новой строки.
text = "hello\nworld"
print(f"38. {text.splitlines() = }")  # ['hello', 'world']

# 39. startswith(prefix, start, end) - Проверяет, начинается ли строка с указанного префикса.
text = "hello world"
print(f"39. {text.startswith('hello') = }")  # True

# 40. strip(chars) - Удаляет начальные и конечные символы, указанные в chars (по умолчанию пробелы).
text = "   hello   "
print(f"40. {text.strip() = }")  # "hello"

# 41. swapcase() - Меняет регистр всех символов строки на противоположный.
text = "Hello World"
print(f"41. {text.swapcase() = }")  # "hELLO wORLD"

# 42. title() - Преобразует строку в заголовок (каждое слово начинается с заглавной буквы).
text = "hello world"
print(f"42. {text.title() = }")  # "Hello World"

# 43. translate(table) - Преобразует строку, используя таблицу преобразований.
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
text = "hello world"
print(f"43. {text.translate(trantab) = }")  # "h2ll4 w4rld"

# 44. upper() - Преобразует все символы строки в верхний регистр.
text = "hello"
print(f"44. {text.upper() = }")  # "HELLO"

# 45. zfill(width) - Дополняет строку нулями слева до указанной ширины.
text = "42"
print(f"45. {text.zfill(5) = }")  # "00042"
