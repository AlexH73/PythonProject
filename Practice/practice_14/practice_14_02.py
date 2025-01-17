# Задача 2: доработать программу из задачи 1, чтобы программа могла играть в крестики-нолики любого размера.

# Основные изменения:
#
#     create_game_map(size): Функция создает игровое поле заданного размера.
#     Размер поля: Функция main запрашивает размер поля у пользователя.
#     Динамическое создание: Игровое поле создается динамически с помощью create_game_map(size).
#     Универсальная проверка: Функции game_map_dash, game_map_user, game_map_bot, check_winner,
#     check_draw теперь принимают game_map в качестве параметра и работают с любым размером поля.
import random


def create_game_map(size):
    """Создает игровое поле заданного размера."""
    return [[None for _ in range(size)] for _ in range(size)]


def game_map_dash(game_map):
    """Выводит текущее состояние игрового поля."""
    size = len(game_map)
    print(" x  " + "  ".join(map(str, range(size))))  # Нумерация столбцов
    print("y  " + "---" * size)
    for y, row in enumerate(game_map):  # Перебираем строки
        print(f"{y} |", end=" ")  # Нумерация строк
        for cell in row:  # Перебираем ячейки в строке
            if cell is None:
                print("_", end="  ")
            else:
                print(cell, end="  ")
        print()


def game_map_user(game_map):
    """
    Позволяет пользователю сделать ход, вводя координаты клетки.
    Возвращает True, если ход успешен, иначе False.
    """
    size = len(game_map)
    while True:  # Повторяем ввод, пока не получим корректные координаты
        try:
            x, y = map(int, input(
                f"Введите координаты (x y) через пробел (например, 0 1) (размер поля {size}x{size}): ").split())
            if not (0 <= x < size and 0 <= y < size):
                print(f"Ошибка: Координаты должны быть целыми числами от 0 до {size - 1}.")
                continue
            if game_map[y][x] is not None:
                print("Ошибка: Эта клетка уже занята. Попробуйте другую.")
                continue
            game_map[y][x] = "X"  # Записываем ход пользователя
            return True
        except ValueError:
            print("Ошибка: Некорректный ввод. Введите два целых числа через пробел.")


def game_map_bot(game_map):
    """Реализует ход бота, выбирая случайную свободную клетку."""
    free_cells = []  # Список свободных клеток
    size = len(game_map)
    for y in range(size):
        for x in range(size):
            if game_map[y][x] is None:
                free_cells.append((x, y))
    if free_cells:  # Если есть свободные клетки
        x, y = random.choice(free_cells)  # Выбираем случайную свободную клетку
        game_map[y][x] = "O"  # Записываем ход бота


def check_winner(game_map, player):
    """
    Проверяет, есть ли победитель на поле для заданного игрока.
    Возвращает True, если есть победа, иначе False.
    """
    size = len(game_map)

    # Проверка горизонталей
    for row in game_map:
        if all(cell == player for cell in row):
            return True

    # Проверка вертикалей
    for x in range(size):
        if all(game_map[y][x] == player for y in range(size)):
            return True

    # Проверка диагоналей
    if all(game_map[i][i] == player for i in range(size)):
        return True
    if all(game_map[i][size - 1 - i] == player for i in range(size)):
        return True
    return False


def check_draw(game_map):
    """Проверяет, есть ли ничья на поле (нет свободных клеток)."""
    for row in game_map:
        if None in row:
            return False
    return True


def main():
    """Основная функция игры."""
    while True:
        try:
            size = int(input("Введите размер игрового поля (например, 3 для 3x3): "))
            if size < 3:
                print("Размер поля должен быть не меньше 3.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    game_map = create_game_map(size)  # Создаем игровое поле нужного размера

    print(f"Добро пожаловать в игру Крестики-нолики {size}x{size}!\n")
    game_map_dash(game_map)  # Выводим начальное состояние поля
    while True:  # Основной игровой цикл
        # Ход пользователя
        while not game_map_user(game_map):
            pass  # Повторяем ход пользователя, пока ввод некорректен
        game_map_dash(game_map)  # Выводим текущее состояние поля

        if check_winner(game_map, "X"):
            print("\nПоздравляем! Вы победили!")
            break
        if check_draw(game_map):
            print("\nНичья! На поле не осталось свободных клеток.")
            break

        # Ход бота
        print("\nХод бота...")
        game_map_bot(game_map)
        game_map_dash(game_map)  # Выводим текущее состояние поля

        if check_winner(game_map, "O"):
            print("\nБот победил! Не расстраивайтесь, повезет в другой раз.")
            break
        if check_draw(game_map):
            print("\nНичья! На поле не осталось свободных клеток.")
            break


# ------- Запуск игры -------
main()
