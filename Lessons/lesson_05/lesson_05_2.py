"""
Метод .format()

Метод .format() позволяет вставлять значения в строку, используя фигурные скобки {}. Это более гибкий способ, который заменил старый стиль.
"""
name = input("Enter your name please ")
age = int(input("How old are you? "))
year_of_birth = 2024 - age

print("Hello %s, nice to meet you! Your year of birth is %d" % (name, year_of_birth))
print("Hello {}, nice to meet you! Your year of birth is {}".format(name, year_of_birth))

"""
#age = input("How old are you? ")
#year_of_birth = 2024 - age
#print("Your year of birth is %d" % (year_of_birth))

age = input("How old are you? ") # "33" str -> 33 int

# такая конструкция нужна для явного приведения типа данных
# то есть изменения типа данных, в данном случае str -> int (строка в число)
int_age = int(age)

year_of_birth = 2024 - int_age
print("Your year of birth is %d" % (year_of_birth))

height = float(input("How tall are you? Please enter answer in m ").replace(',' , '.'))
#height = float(input("How tall are you? Please enter answer in m "))
height_in_foot = height / 0.3

print("Your height in foot is %.2f" % (height_in_foot))
"""