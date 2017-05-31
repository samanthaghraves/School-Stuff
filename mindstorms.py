import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)
    for i in range(1,37):
        
        sides = 0

        while sides < 4:
            brad.forward(100)
            brad.right(90)
            sides = sides + 1
        brad.right(10)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    angie.speed(3)

def draw_triangle():
    alonz = turtle.Turtle()
    alonz.shape("turtle")
    alonz.color("green")
    sides = 0

    while sides < 3:
        alonz.forward(60)
        alonz.left(120)
        sides = sides + 1
        
draw_shapes()
