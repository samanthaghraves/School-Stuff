import turtle

def draw_rhombus(turtle, size, small_angle):
    for i in range(2):
        turtle.forward(size)
        turtle.right(small_angle)
        turtle.forward(size)
        turtle.right((360-2*small_angle)//2)

def draw_flower(turtle, size, angle):
        for i in range(360//angle):
            draw_rhombus(turtle, size, 60)
            turtle.right(angle)
        turtle.right(90)
        turtle.forward(size*3)

canvas = turtle.Screen()
canvas.colormode(255)
canvas.bgcolor("purple")

sam = turtle.Turtle("turtle")
sam.color("yellow")
sam.shape("turtle")
sam.speed(7)

draw_flower(sam, 100, 5)
