# Преобразование из десятичной системы в другие системы счисления

# Десятичное число
decimal_number = 42

# Преобразование в двоичную систему
binary_number = bin(decimal_number)  # '0b101010'
# bin() добавляет префикс '0b' перед двоичным значением

# Преобразование в восьмеричную систему
octal_number = oct(decimal_number)  # '0o52'
# oct() добавляет префикс '0o' перед восьмеричным значением

# Преобразование в шестнадцатеричную систему
hexadecimal_number = hex(decimal_number)  # '0x2a'
# hex() добавляет префикс '0x' перед шестнадцатеричным значением

# Вывод преобразованных значений
print("Двоичное представление:", binary_number)
print("Восьмеричное представление:", octal_number)
print("Шестнадцатеричное представление:", hexadecimal_number)

# Преобразование из других систем счисления обратно в десятичную

# Двоичное представление в формате строки
binary_str = binary_number  # '0b101010'
# Преобразование из двоичной системы в десятичную
decimal_from_binary = int(binary_str, 2)  # 42

# Восьмеричное представление в формате строки
octal_str = octal_number  # '0o52'
# Преобразование из восьмеричной системы в десятичную
decimal_from_octal = int(octal_str, 8)  # 42

# Шестнадцатеричное представление в формате строки
hexadecimal_str = hexadecimal_number  # '0x2a'
# Преобразование из шестнадцатеричной системы в десятичную
decimal_from_hex = int(hexadecimal_str, 16)  # 42

# Вывод результатов обратного преобразования
print("Обратное преобразование из двоичной в десятичную:", decimal_from_binary)
print("Обратное преобразование из восьмеричной в десятичную:", decimal_from_octal)
print("Обратное преобразование из шестнадцатеричной в десятичную:", decimal_from_hex)
