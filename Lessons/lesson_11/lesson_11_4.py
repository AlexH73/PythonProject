"""
Пользователь вводит числа, а мы должны показать сумму
всех введеных положительных чисел.
Остановить работу цикла можно, если пользователь введет 111
"""

num = int(input("Введите число:\n"))

sum = num

while True:
    num = int(input("Введите число:\n"))
    if num == 111:
        print("Вы ввели ключевое для остановки число 111, цикл остановлен")
        break
    print("код после break")

    if num < 0:
        continue

    sum = sum + num
    print("код после continue")

print(sum)