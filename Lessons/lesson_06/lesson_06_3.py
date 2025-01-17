# аргумент - диаметр круга -> посчитать площадь круга
from sys import path_hooks


def calculate_circle_square(diameter):
    pi = 3.14
    r = diameter / 2
    square = pi * r * r

    print(f"Площадь круга с диаметром {diameter} равна:{square:.3f}")

def message_sender(number, text):
    ##...
    print(f"На номер {number} было отправлено сообщение:\n \"{text}\"")
phone_number = "122336655"
message = "Hello!"


calculate_circle_square(3.15)
calculate_circle_square(320)
calculate_circle_square(0.15)
calculate_circle_square(0.0001)
message_sender(phone_number, message)