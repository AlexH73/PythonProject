# Задача 2: Допустимость для голосования
"""
Напишите метод can_vote(age), который принимает возраст пользователя.
Метод должен вернуть True, если возраст 18 или больше.
Иначе метод должен вернуть False.
"""
def can_vote(age):
    if age >= 18:
        return True
    else:
        return False
print(can_vote(int(input("Введите возраст: "))))