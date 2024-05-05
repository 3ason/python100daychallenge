from turtle import Screen, Turtle

screen = Screen() #window that shows up 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game") 
debug = True

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []
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
    new_segment.penup() #don't draw the path it takes 
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True 
while game_is_on: 
    for seg in segments: 
        seg.forward(20)


screen.exitonclick()