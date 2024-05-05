# Day 20 Building the Famous Snake Game 
- let's divide the project into steps 
    - day 1
        - create the snake body 
        - move the snake 
        - control the snake 
    - day 2 
        - detect collision with food 
        - create a scoreboard
        - detect collision with wall 
        - detect collision with tail 

```Python 
from turtle import Screen, Turtle

screen = Screen() #window that shows up 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game") 
debug = True

starting_positions = [(0,0),(-20,0),(-40,0)]

'''
segment_1 = Turtle("square")
segment_1.color("white")
segment_1 = Turtle("square")
segment_1.color("white")
segment_1.goto(-20,0)
segment_1 = Turtle("square")
segment_1.color("white")
segment_1.goto(-40,0)
'''
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
```

# Animating the Snake Segments on Screen 