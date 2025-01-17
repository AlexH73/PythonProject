"""
Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой:

    Есть хотя бы 3 цифры
    Есть хотя бы одна заглавная буква
    Есть хотя бы один символ из следующего набора "!@#$%*"
    Общая длина не менее 10 символов

Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

Вам необходимо написать только определение функции check_password
"""
def check_password(password):
    # Проверка длины пароля
    if len(password) < 10:
        print("Пароль слишком короткий")
        return False

    # Проверка наличия хотя бы 3 цифр
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    if digit_count < 3:
        print("Пароль должен содержать хотя бы 3 цифры")
        return False

    # Проверка наличия хотя бы одной заглавной буквы
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        print("Пароль должен содержать хотя бы одну заглавную букву")
        return False

    # Проверка наличия хотя бы одного специального символа
    special_characters = "!@#$%*"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        print("Пароль должен содержать хотя бы один специальный символ (!@#$%*)")
        return False

    print("Пароль сложный")
    return True


# Пример использования
password = input("Введите пароль для проверки: ")
check_password(password)