# Задача 3: разработать игру "угадай слово".
# Детали:
# 1. Программа выбирает случайное слово из списка.
# 2. Игрок должен угадать это слово, вводя по одной букве.
# 3. Если буква есть в слове, она появляется в нужном месте.
# 4. Игра заканчивается, когда игрок угадывает все буквы в слове или когда он использует все свои попытки.
# 5. В конце игры выводится результат: победа игрока, поражение или ничья.
import random

def choose_word():
    """Выбирает случайное слово из списка."""
    words = ["python", "java", "javascript", "kotlin", "swift", "ruby"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Отображает слово с угаданными и неугаданными буквами."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    """Основная функция игры."""
    secret_word = choose_word()  # Выбираем случайное слово
    guessed_letters = []  # Список уже названных букв
    attempts = 6  # Количество попыток
    game_over = False # Флаг для завершения игры

    print("Добро пожаловать в игру 'Угадай слово'!")
    print(f"У вас {attempts} попыток.")

    while attempts > 0 and not game_over:  # Основной игровой цикл
        print("\nСлово:", display_word(secret_word, guessed_letters))  # Выводим зашифрованное слово
        guess = input("Введите букву: ").lower()  # Получаем букву от пользователя

        if not guess:  # Проверка на пустой ввод
            print("Пожалуйста, введите букву.")
            continue

        if len(guess) != 1 or not guess.isalpha():  # Проверка на корректный ввод
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:  # Проверка, что буква не названа ранее
            print("Вы уже называли эту букву.")
            continue

        guessed_letters.append(guess) # Добавляем букву в список использованных букв


        if display_word(secret_word, guessed_letters) == secret_word:  # Проверка, что слово угадано полностью
          print("\nПоздравляю! Вы угадали слово:", secret_word)
          game_over = True
        elif guess not in secret_word:
          attempts -= 1
          print(f"Не угадали. Осталось попыток: {attempts}")




    if not game_over:
        print("\nВы проиграли! Загаданное слово было:", secret_word)  # Если все попытки использованы

# ------- Запуск игры -------
main()
 # dorabotat#
