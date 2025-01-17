"""
print("Enter your name please!")
name = input()
print("Hello, my name is", name)

city = input("Where are your from? ")
print("%s is a beautiful place!" % (city))

#age = input("How old are you? ")
#year_of_birth = 2024 - age
#print("Your year of birth is %d" % (year_of_birth))

age = input("How old are you? ") # "33" str -> 33 int

# такая конструкция нужна для явного приведения типа данных
# то есть изменения типа данных, в данном случае str -> int (строка в число)
int_age = int(age)

year_of_birth = 2024 - int_age
print("Your year of birth is %d" % (year_of_birth))
"""
height = float(input("How tall are you? Please enter answer in m ").replace(',' , '.'))
#height = float(input("How tall are you? Please enter answer in m "))
height_in_foot = height / 0.3

print("Your height in foot is %.2f" % (height_in_foot))