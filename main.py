import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python turtle")

turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(50)
def rotate_angle_down():
    turtle_instance.setheading(270)
    turtle_instance.forward(50)
def rotate_angle_up():
    turtle_instance.setheading(90)
    turtle_instance.forward(50)
def rotate_angle_right():
    turtle_instance.setheading(0)
    turtle_instance.forward(50)

def rotate_angle_left():
    turtle_instance.setheading(180)
    turtle_instance.forward(50)
def rotate_down_angle():
    turtle_instance.right(50)
def clear_screen():
    turtle_instance.clear()
def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()



drawing_board.listen()
drawing_board.onkey(fun=rotate_down_angle,key="j")
drawing_board.onkey(fun=rotate_angle_left,key="Left")
drawing_board.onkey(fun=rotate_angle_right,key="Right")
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_down,key="Down")
drawing_board.onkey(fun=rotate_angle_up,key="Up")
drawing_board.onkey(fun=clear_screen,key="l")
drawing_board.onkey(fun=turtle_return_home,key="h")



turtle.mainloop()