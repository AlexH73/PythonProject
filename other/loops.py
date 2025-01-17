# 1. for loop - Итерация по элементам итерируемого объекта.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"1_{number}. {number = }")  # 1, 2, 3, 4, 5

# 2. while loop - Выполнение блока кода, пока условие истинно.
count = 0
while count < 5:
    print(f"2_{number}. {count = }")  # 0, 1, 2, 3, 4
    count += 1

# 3. nested loops - Вложенные циклы.
for i in range(3):
    for j in range(2):
        print(f"3. i = {i}, j = {j}")  # i = 0, j = 0; i = 0, j = 1; i = 1, j = 0; i = 1, j = 1; i = 2, j = 0; i = 2, j = 1

# 4. break statement - Прерывание цикла.
for number in numbers:
    if number == 3:
        break
    print(f"4. {number = }")  # 1, 2

# 5. continue statement - Переход к следующей итерации цикла.
for number in numbers:
    if number == 3:
        continue
    print(f"5. {number = }")  # 1, 2, 4, 5

# 6. else clause with for loop - Выполнение блока кода после завершения цикла.
for number in numbers:
    print(f"6. {number = }")  # 1, 2, 3, 4, 5
else:
    print("6. Loop completed")

# 7. else clause with while loop - Выполнение блока кода после завершения цикла.
count = 0
while count < 5:
    print(f"7. {count = }")  # 0, 1, 2, 3, 4
    count += 1
else:
    print("7. Loop completed")
