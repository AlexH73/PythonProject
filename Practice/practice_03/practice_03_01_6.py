# Задание 6: Комбинированное использование методов
"""
Создайте строку с текстом "  Hello, PYTHON WORLD!  ".
- Удалите пробелы в начале и конце строки.
- Преобразуйте строку в нижний регистр.
- Замените слово "python" на "Java".
"""
# Создаем строку
text = "  Hello, PYTHON WORLD!  "

# Удаляем пробелы в начале и конце строки
trimmed_text = text.strip()

# Преобразуем строку в нижний регистр
lowercase_text = trimmed_text.lower()

# Заменяем слово "python" на "Java"
final_text = lowercase_text.replace("python", "java")

# Выводим результат
print(final_text)
