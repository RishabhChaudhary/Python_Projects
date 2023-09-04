from turtle import Turtle, Screen
import random as rd

tipu = Turtle()
screen = Screen()
screen.colormode(255)

tipu.shape('turtle')
tipu.color("#008080")

colors = ["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue","skyblue","cyan","turquoise","lightgreen","green","darkgreen","chocolate","brown","black"]

# for i in range(1, 30):
#     col = rd.choice(colors) if i % 2 == 0 else "white"
#     tipu.pencolor(col)
#     tipu.forward(10)

# for i in range(1, 30):
#     col = rd.choice(colors) 
#     tipu.penup() if i % 2 == 0 else tipu.pendown()
#     tipu.pencolor(col)
#     tipu.forward(10)

# for i in range(3, 10):
#     angle = 360/i
#     side = 100
#     for j in range(i):
#         col = rd.choice(colors)
#         tipu.pencolor(col)        
#         tipu.forward(side)
#         tipu.right(angle)

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)

    return (r,g,b)

# Random Walk
# for i in range(100):
#     angle = rd.choice([0, 90, 180, 270])
#     col = random_color()
#     tipu.pensize(10)
#     tipu.color(col)        
#     tipu.forward(30)
#     tipu.right(angle)

# Circle
# for i in range(int(360/5)):
#     col = random_color()
#     tipu.pensize(2)
#     tipu.speed('fastest')
#     tipu.pencolor(col)
#     tipu.circle(100)
#     cur_head = tipu.heading()
#     tipu.setheading(cur_head + 5)

# Hirst Painting
tipu.penup()
tipu.setx(-400)
tipu.sety(-300)
turn = "l"
for i in range(1, 101):
    col = random_color()
    tipu.fillcolor(col)
    if i % 10 == 0 and turn == "l":
        # print(i)
        tipu.dot(20, col)
        tipu.left(90)
        tipu.forward(40)
        tipu.left(90)
        turn = "r"
        continue
    elif i % 10 == 0 and turn == "r":
        tipu.dot(20, col)
        tipu.right(90)
        tipu.forward(40)
        tipu.right(90)
        turn = "l"
        continue
    tipu.dot(20, col)
    tipu.forward(40)





screen.exitonclick()






