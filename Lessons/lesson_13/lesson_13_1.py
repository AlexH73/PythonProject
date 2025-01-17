# Задачи
# 0.1 сформировать список из книг, при этом сделать это в три шага:
#        1. пустой список
#        2. заполнить тремя значениями
#        3. заменить вторую книгу на "Горе от ума"
#        4. поменять местами значения последнего и первого элементов
my_list = []
my_list[:] = ["Война и мир", "Гарри Поттер", "Алиса в стране чудес"]
my_list[1] = "Горе от ума"
print(my_list)
# более общий подход чтобы менять местами значения списка
# word_of_list = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = my_list[0]
my_list[0], my_list[2] = my_list[2], my_list[0] # меняем местами элементы
print(my_list)

# 0.2 сформировать список из людей, при этом сделать это в три шага:
#        1. определить явно список из трех элементов
#        2. удалить последний элемент
#        3. заменим первое и второе значение на Макса и Ваню
#        4. добавим Сергея в серидну
#        5. добавить Антона и Марию в конец списка
human_list = ["Вася", "Сергей", "Алексей"]
print(human_list)
human_list.pop(-1)
print(human_list)
human_list[0:2] = ["Макс", "Ваня"]
print(human_list)
human_list.insert(1, "Сергей")
print(human_list)
human_list.extend(["Антон", "Мария"])
print(human_list)