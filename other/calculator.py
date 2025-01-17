def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"

    is_negative = decimal_number < 0
    decimal_number = abs(decimal_number)

    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

    # Если число отрицательное, преобразуем в дополнительный код (8 бит)
    if is_negative:
        # Дополняем до 8 бит
        while len(binary_number) < 8:
            binary_number = '0' + binary_number
        # Инвертируем биты
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary_number)
        # Добавляем 1 к инвертированному
        binary_number = bin(int(inverted, 2) + 1)[2:]

        # Убедимся, что длина остается 8 бит
        binary_number = binary_number[-8:]

    return binary_number


def split_binary_by_bytes(binary_string):
    # Дополняем строку нулями слева до кратности 8
    while len(binary_string) % 8 != 0:
        binary_string = '0' + binary_string

    # Разделяем строку на части по 8 символов
    byte_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    # Соединяем части с использованием символа "|"
    return ' | '.join(byte_chunks)


def split_octal(octal_string):
    # Разделяем строку на части по 3 символа
    octal_chunks = [octal_string[i:i + 3] for i in range(0, len(octal_string), 3)]
    return ' | '.join(octal_chunks)


def split_hexadecimal(hex_string):
    # Разделяем строку на части по 2 символа
    hex_chunks = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]
    return ' | '.join(hex_chunks)


# Пример использования
decimal_number = int(input("Введите десятичное число: "))

# Перевод в бинарную систему
binary_number = decimal_to_binary(decimal_number)
binary_with_delimiter = split_binary_by_bytes(binary_number)

# Перевод в восьмеричную и шестнадцатеричную системы
octal_number = oct(decimal_number)[2:]  # Убираем префикс '0o'
hexadecimal_number = hex(decimal_number)[2:]  # Убираем префикс '0x'

# Разделяем восьмеричное и шестнадцатеричное представления
octal_with_delimiter = split_octal(octal_number)
hexadecimal_with_delimiter = split_hexadecimal(hexadecimal_number)

print(f"Десятичное число: {decimal_number}")
print(f"Бинарное число (по байтам): {binary_with_delimiter}")
print(f"Восьмеричное число (по группам по 3): {octal_with_delimiter}")
print(f"Шестнадцатеричное число (по группам по 2): {hexadecimal_with_delimiter}")