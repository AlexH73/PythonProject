# Задание 8: Расширенная таблица
"""
Создайте переменные:
- product1 = "Яблоки", price1 = 1.50, quantity1 = 10, total1 = price1 * quantity1
- product2 = "Груши", price2 = 2.00, quantity2 = 5, total2 = price2 * quantity2
- product3 = "Сливы", price3 = 1.00, quantity3 = 8, total3 = price3 * quantity3
Выведите таблицу:
"""
"""
Товар           Цена      Количество     Сумма
Яблоки          1.50       10             15.00
Груши           2.00       5              10.00
Сливы           1.00       8              8.00
"""
# Создаем переменные
product1 = "Яблоки"
price1 = 1.50
quantity1 = 10
total1 = price1 * quantity1

product2 = "Груши"
price2 = 2.00
quantity2 = 5
total2 = price2 * quantity2

product3 = "Сливы"
price3 = 1.00
quantity3 = 8
total3 = price3 * quantity3

# Выводим таблицу с разделителями строк и столбцов
print("-" * 55)
print(f"{'Товар':<15} | {'Цена':<10} | {'Количество':<15} | {'Сумма':<10}")
print("-" * 55)
print(f"{product1:<15} | {price1:<10.2f} | {quantity1:<15} | {total1:<10.2f}")
print(f"{product2:<15} | {price2:<10.2f} | {quantity2:<15} | {total2:<10.2f}")
print(f"{product3:<15} | {price3:<10.2f} | {quantity3:<15} | {total3:<10.2f}")
print("-" * 55)
