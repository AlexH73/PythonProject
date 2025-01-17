array_of_books = ["Война и мир", "Гарри Поттер", "Алиса в стране чудес"]
i = 0

for book in array_of_books:
    print(book, i)
    i += 1


# 4. Как заменить все семерки в списке на шестерки

array_of_numbers = [8, 4, 7, 3, 9, 7, 5]

# первый вариант
for index in range(len(array_of_numbers)):
    if array_of_numbers[index] == 7:
        array_of_numbers[index] = 6

# второй вариант
for number in array_of_numbers:
    if number == 7:
        index = array_of_numbers.index(number)
        array_of_numbers[index] = 6
        
# третий вариант, наиболее оптимальный
for index, number in enumerate(array_of_numbers):
    if number == 7:
        array_of_numbers[index] = 6

# ----

