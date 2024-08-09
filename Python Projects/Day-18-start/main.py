from turtle import Turtle, Screen

surqash = Turtle()
# surqash.shape("turtle")
surqash.color("green")


def triangle():
        for _ in range(3):
                surqash.right(120)
                surqash.forward(100)


def square():
        for _ in range(4):
                surqash.pencolor("red")
                surqash.right(90)
                surqash.forward(100)


def pentagon():
        for _ in range(5):
                surqash.pencolor("blue")
                surqash.right(72)
                surqash.forward(100)


def hexagon():
        for _ in range(6):
                surqash.pencolor("orange")
                surqash.right(60)
                surqash.forward(100)


def octagon():
        for _ in range(7):
                surqash.pencolor("purple")
                surqash.right(51.4285714)
                surqash.forward(100)


def nonagon():
        for _ in range(8):
                surqash.pencolor("black")
                surqash.right(45)
                surqash.forward(100)


def decagon():
        for _ in range(9):
                surqash.pencolor("crimson")
                surqash.right(40)
                surqash.forward(100)


triangle()
square()
pentagon()
hexagon()
octagon()
nonagon()
decagon()


screen = Screen()
screen.exitonclick()