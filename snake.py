import turtle
import random
import time

# background screen
screen = turtle.Screen()
screen.title("SNAKE-GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("Black")

# border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("Midnight Blue")
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.penup()
border.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.color("Deep Sky Blue")
snake.shape("square")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Tomato")
food.penup()
food.goto(30, 30)

segments = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))


# movement functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


def end_game():
    global game_running
    game_running = False
    # Hide all game elements
    snake.hideturtle()
    food.hideturtle()
    for segment in segments:
        segment.hideturtle()
    # Clear the screen except the scoring
    screen.clear()
    screen.bgcolor("Dark Slate Blue")
    scoring.goto(0, 0)
    scoring.write(f"  Game over \n Your score is {score}", align="center", font=("Courier", 24, "bold"))


# game loop
game_running = True
while game_running:
    screen.update()

    # check for collision with food
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)

        # add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("Deep Sky Blue")
        new_segment.penup()
        segments.append(new_segment)

        # update the score
        score += 1
        scoring.clear()
        scoring.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # check for collision with border
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        end_game()

    # check for collision with itself
    for segment in segments:
        if segment.distance(snake) < 20:
            end_game()

    if game_running:
        time.sleep(delay)


# Wait for a key press to close the window
def close_game():
    screen.bye()


screen.onkeypress(close_game, "q")
screen.listen()
screen.mainloop()
