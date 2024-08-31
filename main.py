import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# The Player class initiates the turtle
turtle = Player()
turtle.turtle_position()
turtle.finish_line()

# Creating the Car_Manager class
cars = CarManager()

# Adding the score
level = Scoreboard()
level.write_score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.move()
    turtle.finish_line()
    cars.create_car()
    cars.move_cars()
    # Checking the collision with the cars
    for car in cars.cars:
        if turtle.xcor() + 20 > car.xcor() > turtle.xcor() - 20:
            if turtle.ycor() + 20 > car.ycor() > turtle.ycor() - 20:
                game_is_on = False
                level.write_game_over()
                break

    # Passing the level

    if turtle.finish_line():
        level.increase_score()
        turtle.turtle_position()  # Reset the turtle position
        cars.increase_speed(100)  # You might adjust the speed increment here

screen.exitonclick()
