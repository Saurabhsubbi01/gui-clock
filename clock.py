import time
import datetime as dt
import turtle

# Create a turtle to display time
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
clock_turtle.penup()

# Create a turtle to create a rectangular box
box_turtle = turtle.Turtle()
box_turtle.pensize(3)
box_turtle.hideturtle()

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set the position of the rectangular box
box_turtle.penup()
box_turtle.goto(-100, -35)
box_turtle.pendown()

# Create rectangular box
for _ in range(2):
    box_turtle.forward(200)
    box_turtle.left(90)
    box_turtle.forward(70)
    box_turtle.left(90)

# Hide the turtle
box_turtle.hideturtle()

# Function to update time
def update_time():
    sec = dt.datetime.now().second
    minute = dt.datetime.now().minute
    hour = dt.datetime.now().hour

    clock_turtle.clear()

    # Display the time
    clock_turtle.color("white")
    clock_turtle.goto(0, 0)
    clock_turtle.write(
        str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2),
        align="center",
        font=("Arial", 40, "bold")
    )

    screen.update()
    screen.ontimer(update_time, 1000)

# Call the function to update time
update_time()

# Keep the window open
screen.mainloop()
