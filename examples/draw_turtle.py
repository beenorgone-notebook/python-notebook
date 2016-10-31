import turtle

def draw_square(any_turtle):
    for i in range (0, 4):
        any_turtle.forward(100)
        any_turtle.right(90)

def draw_circle(any_turtle):
    any_turtle.circle(100)

def draw_equilateral_triangle(any_turtle):
    for i in range (0, 3):
        any_turtle.forward(100)
        any_turtle.right(120)

def draw_flower(any_turtle):
    for i in range(0, 36):
        draw_square(any_turtle)
        any_turtle.right(10)

def turtle_def(t_name, t_color, t_shape, t_speed):
    t_name = turtle.Turtle()
    t_name.color(t_color)
    t_name.shape(t_shape)
    t_name.speed(t_speed)
    return t_name

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("violet")

    #Diego
    draw_flower(turtle_def("diego", "gray", "circle", "fast"))
    #Angie
    draw_circle(turtle_def("angie", "blue", "arrow", None))
    #Brad
    draw_square(turtle_def("brad", "yellow", "turtle", 2))
    #Justin
    draw_equilateral_triangle(turtle_def("justin", "green", "classic", 1))

    window.exitonclick()

draw_shape()
