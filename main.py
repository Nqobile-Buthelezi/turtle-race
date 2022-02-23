import random
from turtle import Turtle, Screen

screen = Screen()

is_race_on = True

user_bet = screen.textinput(title="Make your bet", prompt="Who do you think will win? Enter a color: ")
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
color_position = 0
starting_y = -90

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color_position])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y)
    starting_y += 30
    color_position += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The winning colour is {winning_color}.")
            else:
                print(f"You lose, the winning colour is {winning_color}.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
