class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} говорит: Гав-гав!"

# Пример использования метода
my_dog = Dog("Бобик")
print(my_dog.bark())
