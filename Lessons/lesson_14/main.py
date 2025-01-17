import random

def guess_number(start, end):
    rand_number = random.randint(start, end) # случайное число от 1 до 10
    user_number = int(input("Введите число от 1 до 10: "))

    if rand_number == user_number:
        print("Вы угадали число!")
    else:
        print(f"Вы не угадали число! Правильный ответ: {rand_number}")


def main():
    while True:
        guess_number()

        if input("Хотите сыграть еще раз? (y/n): ") == "n":
            break


if __name__ == "__main__":
    main()
