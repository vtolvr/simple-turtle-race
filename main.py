import turtle
import random

def setup_turtles(num_turtles):
    turtles = []
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    for i in range(num_turtles):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(colors[i % len(colors)])
        t.penup()
        t.goto(-200, 100 - i * 30)
        turtles.append(t)
    return turtles

def race(turtles):
    for _ in range(100):
        for t in turtles:
            t.forward(random.randint(1, 10))
    turtle.done()

turtle.setup(800, 600)
turtles = setup_turtles(6)
race(turtles)
