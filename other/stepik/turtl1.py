import turtle, math

# общие настройки экрана
# задаем размер и цвет фона
win = turtle.Turtle()
win.screen.setup(1000, 400)
win.screen.bgcolor('black')

# создаем планеты
planet = turtle.Turtle()
planet.hideturtle()

# создаем солнце и задаем ему условный диаметр
sun = turtle.Turtle()
sun.hideturtle()
# SUN
# D = 1390000
S = 1000
sun.up()
sun.goto(-700, 250)
sun.down()
sun.dot(S, 'yellow')
sun.up()
sun.goto(-400, 50)
sun.color('red')
sun.write('SUN', move=False, align="center", font=('verdana', 12, 'normal'))


# функция рисует овал
def drawoval(rad):
    for x in range(2):
        planet.circle(rad, 90)
        planet.circle(rad // 2, 90)


# РАЗМЕРЫ ПЛАНЕТ ОТРИСОВЫВАЮТСЯ ПРОПОРЦИОНАЛЬНО РАЗМЕРАМ СОЛНЦА

# mercury
# D = 4879
planet.up()
planet.goto(-200, 0)
planet.down()
planet.dot(S // 284, '#e5e5e5')
planet.up()
planet.setheading(-90)
planet.forward(25)
planet.down()
planet.color('red')
planet.write('Mercury', move=False, align="center", font=("Verdana", 8, "normal"))

## venus
# = 12100
planet.up()
planet.goto(-123, 0)
planet.down()
planet.dot(S // 114, '#928590')
planet.up()
planet.setheading(-90)
planet.forward(27)
planet.down()
planet.color('red')
planet.write('Venus', move=False, align="center", font=("Verdana", 8, "normal"))

## earth
# D = 12750
planet.up()
planet.goto(-44.5, 0)
planet.down()
planet.dot(S // 109, '#a2653e')
planet.up()
planet.setheading(-90)
planet.forward(27)
planet.down()
planet.color('red')
planet.write('Earth', move=False, align="center", font=("Verdana", 8, "normal"))

## mars
# D = 6790
planet.up()
planet.goto(28, 0)
planet.down()
planet.dot(S // 205, '#964514')
planet.up()
planet.setheading(-90)
planet.forward(27)
planet.down()
planet.color('red')
planet.write('Mars', move=False, align="center", font=("Verdana", 8, "normal"))

## jupiter
# D = 142984
planet.up()
planet.goto(120.5, 0)
planet.down()
planet.dot(S // 9, '#9abeb7')
planet.up()
planet.setheading(-90)
planet.forward(75)
planet.down()
planet.color('red')
planet.write('Jupiter', move=False, align="center", font=("Verdana", 8, "normal"))

# saturn
# D = 120420
planet.up()
planet.goto(262.5, 0)
planet.down()
planet.dot(S // 11, '#c4bcaa')
#
planet.up()
planet.setheading(-90)
planet.forward(80)
planet.down()
planet.color('red')
planet.write('Saturn', move=False, align="center", font=("Verdana", 8, "normal"))
x = 225.5
y = -65
for i in range(4):
    planet.up()
    planet.goto(x + i * 2.5, y + i * 3.5)
    planet.seth(-10)
    planet.down()
    planet.color('#cecece')
    drawoval(98 - i * 7)

# uranus
# D = 51300
planet.up()
planet.goto(375, 0)
planet.down()
planet.dot(S // 27, '#3d4e70')
planet.up()
planet.setheading(-90)
planet.forward(50)
planet.down()
planet.color('red')
planet.write('Uranus', move=False, align="center", font=("Verdana", 8, "normal"))
# да, у Урана тоже есть свои кольца!
planet.up()
planet.goto(386, -25)
planet.down()
planet.seth(40)
planet.color('#cecece')
drawoval(35)

# neptune
# D = 49500
planet.up()
planet.goto(450, 0)
planet.down()
planet.dot(S // 28, '#4d8fac')
planet.up()
planet.setheading(-90)
planet.forward(50)
planet.down()
planet.color('red')
planet.write('Neptune', move=False, align="center", font=("Verdana", 8, "normal"))

turtle.done()