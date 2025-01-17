# список продуктов

"""
Список продуктов

1. яблоко
2. банан
3. апельсин
4. киви
"""

products = ["яблоко", "банан", "апельсин", "киви"] 

print(products[0]) # яблоко

a = []

a.append(10)
a.append(20)
a.append(30)
a.append(-40)
a.append(55)

a[1] = 7

print(a[1])

a[3:5] = [777, 888]

print(a[3:5])

print(a[-1]) # последний элемент

# ---

a.extend([1,2,3,4])  # добавление сразу нескольких значений в конец

a.insert(0, 1234567)  # добавление числа 1234567 на позицию с индексом 0
a.insert(2, 976454)  # добавление числа 976454 на позицию с индексом 2

a.pop(3)  # удаление элемента под индексом 3

if 10 in a:  # проверка на вхождение числа 10 в наш список 
    index_of_10 = a.index(10)  # поиск значения в списке, вернет индекс первого подходящего значения
    value = a[index_of_10]
    print(value)

# ---
# Задачи
# 0.1 сформировать список из книг, при этом сделать это в три шага:
#        1. пустой список
#        2. заполнить тремя значениями
#        3. заменить вторую книгу на "Горе от ума"
#        4. поменять местами значения последнего и первого элементов

my_list = []
my_list[:] = ["Война и мир", "Гарри Поттер", "Алиса в стране чудес"]
my_list[1] = "Горе от ума"

# более общий подход чтобы менять местами значения списка
# word_of_list = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = my_list[0]

my_list[0], my_list[2] = my_list[2], my_list[0] # меняем местами элементы

# 0.2 сформировать список из людей, при этом сделать это в три шага:
#        1. определить явно список из трех элементов
#        2. удалить последний элемент
#        3. заменим первое и второе значение на Макса и Ваню
#        4. добавим Сергея в серидну
#        5. добавить Антона и Марию в конец списка


human_list = ["Вася", "Сергей", "Алексей"]

human_list.pop(-1)

human_list[0:2] = ["Макс", "Ваня"]

human_list.insert(1, "Сергей")

human_list.extend(["Антон", "Мария"])







cookies = ["печенье 1", "печенье 2", "печенье 3", "печенье 4"]

cookies_of_karl = cookies

cookies_of_anton = cookies

print(cookies_of_karl[1])  # "печенье 2"
print(cookies_of_anton[1])  # "печенье 2"

cookies_of_karl[1] = "торт"
print(cookies_of_anton[1])  # "торт"


def func1(values):
    values[0] = "test"
    print(values)


func1(cookies)

print(cookies_of_karl)
# ["test", "торт", "печенье 3", "печенье 4"]

# точка 1
def func2():
    a = [1, 2,3,4,5,5,6]
    print(a)
# точка 2
func2()
# точка 3




my_list_1 = [1,2,3]
my_list_2 = [1,2,3]
my_list_3 = my_list_1

my_list_1[1] = 777
my_list_2[2] = 666
my_list_3[0] = 111

print(my_list_1) # 111 777 3
print(my_list_2) # 1 2 666
print(my_list_3) # 111 777 3





























