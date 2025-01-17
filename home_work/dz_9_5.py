# 5. Проверка надёжности пароля:
"""
Напишите метод is_strong_password, который принимает строку пароля.
Метод должен возвращать True, если пароль содержит не менее 8 символов и включает как буквы, так и цифры.
Иначе метод должен возвращать False.
"""
# Назначаем метод и аргумент
def is_strong_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False

    # Вспомогательная функция для проверки наличия букв
    def has_letter(password):
        if not password:
            return False
        return password[0].isalpha() or has_letter(password[1:])

    # Вспомогательная функция для проверки наличия цифр
    def has_digit(password):
        if not password:
            return False
        return password[0].isdigit() or has_digit(password[1:])

    return has_letter(password) and has_digit(password)

# Ввод строки и вызов функции
password = input("Введите пароль: ")
print(is_strong_password(password))




# Назначаем метод и аргумент
def is_strong_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False

    # Проверка наличия букв и цифр
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_letter and has_digit


# Ввод строки и вызов функции
password = input("Введите пароль: ")
print(is_strong_password(password))


# Назначаем метод и аргумент
def is_strong_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False

    # Проверка наличия букв и цифр
    has_letter = False
    has_digit = False

    # Использование индексов для проверки каждого символа
    i = 0
    while i < len(password):
        if password[i].isalpha():
            has_letter = True
        if password[i].isdigit():
            has_digit = True
        i += 1

    return has_letter and has_digit

# Ввод строки и вызов функции
password = input("Введите пароль: ")
print(is_strong_password(password))


# решение через множества
def is_strong_password(password):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    # содержит не менее 8 символов
    if len(password) < 8:
        return False

    # и включает как буквы
    if not set(password.lower()) & set(letters):
        return False

    # - так и цифры.
    if not set(password.lower()) & set(digits):
        return False

    return True


# решение через циклы
def is_strong_password_2(password_string):
    if len(password_string) < 8:
        return False

    if not any(char.isalpha() for char in password_string):
        return False

    if not any(char.isdigit() for char in password_string):
        return False

    return True
passw = input("Введите пароль: ")
print(is_strong_password(passw))