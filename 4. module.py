#Turtle
import turtle as t
import random

#Bad Turtle
joker = t.Turtle()
joker.shape("turtle")
joker.color("red")
joker.speed(0)
joker.up()
joker.goto(0, 200)

#Food
food = t.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0, -200)

#Direction
def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

#Rules
def play():
    t.forward(10)
    ang = joker.towards(t.pos())
    joker.setheading(ang)
    joker.forward(9)
    if t.distance(food) < 12:
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        food.goto(star_x, star_y)
    if t.distance(joker) >= 12:
        t.ontimer(play, 100)

#Run
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()
t.mainloop()