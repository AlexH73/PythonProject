# Задача 1: разработать игру крестики-нолики для одного игрока, в качестве второго игрока будет выступать сама программа.
# Детали:
# 1. Игровое поле представляет собой квадрат 3x3.
# 2. Игрок и программа ходят по очереди, ставя на свободные клетки поля свои символы (игрок - "X", программа - "O").
# 3. Программа должна иметь простую стратегию для выбора хода (например, случайный выбор).
# 4. Игра заканчивается, когда один из игроков выстраивает три своих символа в ряд по горизонтали,
# вертикали или диагонали, либо когда все клетки поля заняты (ничья).
# 5. После каждого хода необходимо отображать текущее состояние игрового поля.
# 6. В конце игры выводится результат: победа игрока, победа программы или ничья.

"""game_map = [
    [None, None, None],
    [None, "X", None],
    [None, None, "0"]
]
def game_map_user():
    x, y = input("Введите координаты: ").split()
    x = int(x)
    y = int(y)
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    if game_map[y][x] is not None:
        return False
    game_map[y][x] = "X"
    return True
def game_map_bot():
    pass

def main(): # Если game_map_user выдает True то ход передается боту, иначе повторяем ход юзера.
    # Проверка игрового поля.
    pass

def game_map_dash():
    for i in range(3):
        for j in range(3):
            if game_map[i][j] is None:
                print("_", end = " ")
            else:
                print(game_map[i][j], end = " ")
        print("")

game_map_dash()"""

import random

# 1. Игровое поле 3x3
game_map = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def game_map_dash():
    """Выводит текущее состояние игрового поля с нумерацией строк и столбцов."""
    print(" x   0  1  2")  # Нумерация столбцов
    print("y  ---------")
    for y, row in enumerate(game_map): # Перебираем строки с индексом
        print(y, "| ", end=" ")  # Нумерация строк
        for cell in row: # Перебираем ячейки в строке
            if cell is None:
                print("_", end="  ")
            else:
                print(cell, end="  ")
        print()


def game_map_user():
    """
    Позволяет пользователю сделать ход, вводя координаты клетки.
    Возвращает True, если ход успешен, иначе False.
    """
    while True:  # Повторяем ввод, пока не получим корректные координаты
        try:
            x, y = map(int, input("Введите координаты (x y) через пробел (например, 0 1): ").split())
            if not (0 <= x < 3 and 0 <= y < 3):
                print("Ошибка: Координаты должны быть целыми числами от 0 до 2.")
                continue
            if game_map[y][x] is not None:
                print("Ошибка: Эта клетка уже занята. Попробуйте другую.")
                continue
            game_map[y][x] = "X"  # Записываем ход пользователя
            return True
        except ValueError:
            print("Ошибка: Некорректный ввод. Введите два целых числа через пробел.")


def game_map_bot():
    """Реализует ход бота, выбирая случайную свободную клетку."""
    free_cells = [] # Список свободных клеток
    for y in range(3):
        for x in range(3):
            if game_map[y][x] is None:
                free_cells.append((x, y))
    if free_cells:  # Если есть свободные клетки
        x, y = random.choice(free_cells)  # Выбираем случайную свободную клетку
        game_map[y][x] = "O"  # Записываем ход бота


def check_winner(player):
    """
    Проверяет, есть ли победитель на поле для заданного игрока.
    Возвращает True, если есть победа, иначе False.
    """
    # Проверка горизонталей
    for row in game_map:
        if all(cell == player for cell in row):
            return True

    # Проверка вертикалей
    for x in range(3):
        if all(game_map[y][x] == player for y in range(3)):
            return True

    # Проверка диагоналей
    if all(game_map[i][i] == player for i in range(3)):
        return True
    if all(game_map[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    """Проверяет, есть ли ничья на поле (нет свободных клеток)."""
    for row in game_map:
        if None in row:
            return False
    return True


def main():
    """Основная функция игры."""
    print("Добро пожаловать в игру Крестики-нолики!\n")
    game_map_dash()  # Выводим начальное состояние поля
    while True:  # Основной игровой цикл
        # Ход пользователя
        while not game_map_user():
           pass # Повторяем ход пользователя, пока ввод некорректен
        game_map_dash() # Выводим текущее состояние поля

        if check_winner("X"):
            print("\nПоздравляем! Вы победили!")
            break
        if check_draw():
            print("\nНичья! На поле не осталось свободных клеток.")
            break

        # Ход бота
        print("\nХод бота...")
        game_map_bot()
        game_map_dash() # Выводим текущее состояние поля

        if check_winner("O"):
            print("\nБот победил! Не расстраивайтесь, повезет в другой раз.")
            break
        if check_draw():
             print("\nНичья! На поле не осталось свободных клеток.")
             break

# ------- Запуск игры -------
main()