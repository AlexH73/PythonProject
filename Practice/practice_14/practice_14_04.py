# Задача 4: разработать программу, которая умеет зашифровывать и расшифровывать короткие текстовые сообщения методом шрифта Цезаря (или любым другим сдвиговым шифром).
# Детали
# 1. Пользователь вводит сам текст (например, фразу).
# 2. Указывает, хочет он «зашифровать» или «расшифровать» (логический выбор).
# 3. Вводит число сдвига (целое, например, от 1 до 25).
# 4. Программа пробегается по каждой букве во введённом тексте и смещает её в алфавите на заданное количество позиций.
#     - Для «зашифровки» двигаем вперёд (A→C при сдвиге 2).
#     - Для «расшифровки», наоборот, двигаем в обратную сторону.
# 5. Программа игнорирует пробелы, цифры, знаки препинания или обрабатывает их особо — по вашему желанию.
# 6. Выводит результат в консоль (зашифрованную строку или расшифрованную).
# 7. Спрашивает, хочет ли пользователь повторить, и организует цикл (например, while) до тех пор, пока не будет введена команда выхода.
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if encrypt else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char  # Оставляем символы без изменений
    return result


def main():
    while True:
        print("\nПрограмма шифрования/дешифрования текста методом шифра Цезаря")
        text = input("Введите текст: ")

        # Получаем выбор действия
        action = input("Выберите действие ('зашифровать' или 'расшифровать'): ").strip().lower()
        if action not in ("зашифровать", "расшифровать"):
            print("Неверный выбор. Попробуйте снова.")
            continue

        # Получаем сдвиг
        try:
            shift = int(input("Введите сдвиг (целое число от 1 до 25): "))
            if not (1 <= shift <= 25):
                raise ValueError
        except ValueError:
            print("Некорректное число. Попробуйте снова.")
            continue

        # Выполняем действие
        encrypt = action == "зашифровать"
        result = caesar_cipher(text, shift, encrypt)
        print(f"Результат: {result}")

        # Спрашиваем, хочет ли пользователь повторить
        repeat = input("Хотите повторить? (да/нет): ").strip().lower()
        if repeat != "да":
            print("Выход из программы. До свидания!")
            break


if __name__ == "__main__":
    main()
