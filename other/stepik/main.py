

r, c = map(int, input().split())
tort = []
for i in range(r):
    tort.append(input())
mas = [[False] * c for i in range(r)]
for i in range(r):
    if "S" not in tort[i]:
        for j in range(c):
            mas[i][j] = True
for j in range(c):
    is_find = False
    for i in range(r):
        if tort[i][j] == "S":
            is_find = True
            break
    if not  is_find:
        for i in range(r):
            mas[i][j] = True
count = 0
for row in mas:
    count += row.count(True)

print(count)






direction = 'NoRtH'
match direction.lower():
    case "north" | "east" | "south" | "west":
        print("Хорошо, я пошел!")
    case _:
        print("Неизвестное направление...")

a, b, c = 1, 2, 3

if a > b and a > c:
    print(a)
else:
    if b > c and b > a:
        print(b)
    else:
        print(c)

a = 5
b = 7

min, max = (a, b) if a > b else (b, a)
print(max, min)

x = 5
text = "Even" if x % 2 == 0 else "Odd"

print(text)

s = "Hello123"

print(
    '0' in s or '1' in s or '2' in s or '3' in s or '4' in s or '5' in s or '6' in s or '7' in s or '8' in s or '9' in s)

gender = {'m': 'Дорогой', 'f': 'Дорогая'}

people = [
    ['Семён', 'Семёнович', 32.56, 'm'],
    ['Тамара', 'Ивановна', 13.12, 'f'],
    ['Михаил', 'Анатольевич', 238.12, 'm'],
]

for name, midname, balance, g in people:
    message = f"{gender[g]} {name} {midname}, баланс вашего счёта составляет {balance} руб."
    print(message)

print("""
/\\_/\\
>^,^<
 / \\
(|_|)_/

""")

print('  /~~~\\\n //^ ^\\\\\n(/(_*_)\\)\n_/\'\'*\'\'\\_\n(/_)^(_\\)')

name = 'Семён'
surname = 'Семёнов'
balance = 32.56

text = """Дорогой {n} {s},
баланс Вашего лицевого счёта составляет {b} руб.""".format(s=surname, n=name, b=balance)

print(text)
