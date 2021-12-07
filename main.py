# classic snake game
# 01/dec/2021 13:00

# import turtle library classes Turtle and Screen
# import random to use random numbers
# import time module
# import snake to build the individual square objects and move them
# import food to add food at random locations
# import write to keep score and notify if game over
import time
from turtle import Screen
from snake import Snake
from food import Food
from write import Write

# creates screen object and sets its title
screen = Screen()
screen.setup(width=600, height=600)
# screen is set to black
screen.bgcolor('black')
screen.title("Welcome to the snake game!")
# enables the .listen() command in order to accept key commands
screen.listen()
# disables tracer to smooth the transitions from screen to screnn with the .update() and time.sleep()
screen.tracer(0)

# initiations blocks
# initiates the snake code
cobra = Snake()
# initiates the food placement
food = Food()
# initiates the score and game over prompts when necessary
score = Write()
# sets game to start
game_on = True

while game_on:
    # moves the snake and updates the screen only after a complete move is done
    cobra.move()
    screen.update()
    time.sleep(0.1)
    # creates the logic to turn the snake on arrow commands
    screen.onkey(key='Right', fun=cobra.turn_right)
    screen.onkey(key='Up', fun=cobra.turn_up)
    screen.onkey(key='Left', fun=cobra.turn_left)
    screen.onkey(key='Down', fun=cobra.turn_down)

    # detects if the snake head (cobra.snake[0]) is 20 pixels from each side.
    # if so, turns game off, sets game_over routine and resets the screen
    most_far_x = cobra.snake[0].xcor()
    most_far_y = cobra.snake[0].ycor()
    if most_far_x > 280 or most_far_x < -280 or most_far_y > 280 or most_far_y < -280:
        # reinitiates the game
        time.sleep(1)
        score.reset()
        cobra.reset()


    # food detection using the distance method
    # if so, activates plus_one() to extend the body of the snake, places a new food item and updates the score
    if cobra.snake[0].distance(food) < 20:
        food.refresh()
        cobra.plus_one()
        score.clear()
        score.increase_score()

    # detects if (cobra.snake[0]) is touching any other segment
    # if so, turns game off, waits 3 seconds, sets game_over routine and resets the screen
    list_of_positions = []
    i = 0
    for i in range(1,len(cobra.snake)):
        list_of_positions.append(cobra.snake[i].pos())
    if cobra.snake[0].pos() in list_of_positions:
        time.sleep(1)
        score.reset()
        cobra.reset()


# exits screen on click after game is over
screen.exitonclick()

