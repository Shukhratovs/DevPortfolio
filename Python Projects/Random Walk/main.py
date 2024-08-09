import turtle as t
from turtle import Screen
import random

surqash = t.Turtle()
# colors = ["red", "green", "blue", "orange", "purple", "black", "crimson", "tan", "teal", "pale violet red"]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color

# directions = [0, 90, 180, 270]
surqash.speed("fastest")
# surqash.pensize(8)

for _ in range(76):
    surqash.color(random_color())
    surqash.circle(100)
    surqash.right(5)


screen = Screen()
screen.exitonclick()