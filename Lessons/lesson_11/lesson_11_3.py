"""
Напишите программу, которая принимает число N от пользователя
и с помощью цикла while вычисляет сумму всех чисел от 1 до N.

4 = 1 + 2 + 3 + 4 = 10

-10 = 0
0  = 0
num > 20 = 0
"""
"""
n = int(input("Введите число: "))
sum = 0
a = 0
if not (n < 0 or n >= 20):
    while a < n:
        a = a + 1
        sum = sum + a
print(sum)
"""
n = int(input("Введите число: "))
sum = 0
a = 1
if not (n < 0 or n >= 20):
    while a <= n:
        sum = sum + a
        a = a + 1
print(sum)


