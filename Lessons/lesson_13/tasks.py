# 1. Дан список чисел – [8, 4, 7, 3, 9, 2, 5]. 
# Напишите программу, выводит все значения из этого списка на экран – каждое значение с новой строки.

def task_1():
    numbers = [8, 4, 7, 3, 9, 2, 5]
    for number in numbers:
        print(number)

# 2. Дан список чисел – [8, 4, 7, 3, 9, 2, 5]. 
# Напишите программу, которая определяет минимальное значение из этого списка
#    и выводит его в консоль, пользуясь встроенными функциями.

def task_2():
    numbers = [8, 4, 7, 3, 9, 2, 5]
    min_number = min(numbers)
    print(min_number)

# 3. Самостоятельная работа. Дан список чисел – [8, 4, 7, 3, 9, 2, 5]. 
# Напишите программу, которая определяет минимальное

def task_3():
    numbers = [8, 4, 7, 3, 9, 2, 5]
    min_number = numbers[0]
    
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    
    print(min_number)



# 4. Дан список чисел – [8, 4, 7, 3, 9, 2, 5]. 
# Напишите программу, которая суммирует все числа списка и выводит результат на экран.

def task_4():
    array = [8, 4, 7, 3, 9, 2, 5]
    result = sum(array)
    print(result)


def task_4_2():
    array = [8, 4, 7, 3, 9, 2, 5]
    result = 0
    
    for number in array:
        result += number
    
    print(result)

# 5. Дан список имен – ["Иван", "Пётр", "Василий", "Алексей", "Александр"]. 
# Запросите у пользователя его имя. Программа должна вывести на экран один 
# из следующих вариантов – «Ваше имя есть в списке», «Вашего имени нет в списке».

def task_5():
    names = ["Иван", "Пётр", "Василий", "Алексей", "Александр"]
    user_name = input("Your name: ")
    
    if user_name in names:
        print("Ваше имя есть в списке")
    else:
        print("Вашего имени нет в списке")


# 6. Самостоятельная работа. Даны два списка строк – ["A", "B", "C", "D", "E"] и ["D", "E", "F", "G"]. 
# Напишите функцию, которая возвращает третий список, содержащий все элементы обоих списков. 
# Ожидаемый результат - ["A", "B", "C", "D", "E", "D", "E", "F", "G"].

