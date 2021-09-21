import turtle
from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race ? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
y_position = ['-70','-40','-10','20','50','80']
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(float(-230), float(y_position[turtle_index]))
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on :
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won, The {winning_color} turtle is the winner")
            else:
                print(f"You lost, The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

# Small Project - Ede sketch
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun= move_forward )
# screen.onkey(key="s", fun= move_backward )
# screen.onkey(key="a", fun= turn_left )
# screen.onkey(key="d", fun= turn_right )
# screen.onkey(key="c", fun= clear )
# screen.exitonclick()