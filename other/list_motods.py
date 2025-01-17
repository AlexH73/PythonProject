# Методы списков в Python

# 1. Создание списка
lst = [1, 2, 3]

# 2. append(x): Добавляет элемент x в конец списка
lst.append(4)
print(lst)  # Вывод: [1, 2, 3, 4]

# 3. extend(iterable): Расширяет список, добавляя все элементы из переданного итерируемого объекта
lst.extend([5, 6])
print(lst)  # Вывод: [1, 2, 3, 4, 5, 6]

# 4. insert(i, x): Вставляет элемент x на позицию i
lst.insert(1, 7)
print(lst)  # Вывод: [1, 7, 2, 3, 4, 5, 6]

# 5. remove(x): Удаляет первый элемент в списке, значение которого равно x
lst.remove(7)
print(lst)  # Вывод: [1, 2, 3, 4, 5, 6]

# 6. pop([i]): Удаляет элемент на позиции i и возвращает его. Если индекс не указан, удаляется и возвращается последний элемент
lst.pop()
print(lst)  # Вывод: [1, 2, 3, 4, 5]

# 7. clear(): Удаляет все элементы из списка
lst.clear()
print(lst)  # Вывод: []

# 8. index(x[, start[, end]]): Возвращает индекс первого элемента, значение которого равно x. Можно указать начальный и конечный индексы для поиска
lst = [1, 2, 3, 2]
print(lst.index(2))  # Вывод: 1

# 9. count(x): Возвращает количество элементов в списке, значение которых равно x
print(lst.count(2))  # Вывод: 2

# 10. sort(key=None, reverse=False): Сортирует элементы списка на месте
lst.sort()
print(lst)  # Вывод: [1, 2, 2, 3]

# 11. reverse(): Разворачивает элементы списка на месте
lst.reverse()
print(lst)  # Вывод: [3, 2, 2, 1]

# 12. copy(): Возвращает поверхностную копию списка
lst_copy = lst.copy()
print(lst_copy)  # Вывод: [3, 2, 2, 1]
