# 3. Напишите функцию, которая принимает на вход список чисел,
# находит в нём максимальное и минимальное значения, и меняет их местами.

def swap_min_max(numbers):
    if not numbers:  # Если список пустой
        return  # Ничего не делаем

    min_index = numbers.index(min(numbers))  # Индекс минимального значения
    max_index = numbers.index(max(numbers))  # Индекс максимального значения

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]  # Меняем значения местами


# Примеры использования:
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
swap_min_max(numbers)
print(numbers)  # Выведет: [3, 9, 4, 1, 5, 1, 2, 6]

# numbers2 = [5]
# swap_min_max(numbers2)
# print(numbers2) # Выведет [5]

# numbers3 = []
# swap_min_max(numbers3)
# print(numbers3) # Выведет []
