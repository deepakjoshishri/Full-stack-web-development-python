import turtle

window= turtle.Screen()
turtle1= turtle.Turtle()
turtle1.color("#ffcc00","black")
def draw_flower():
    window.bgcolor("#3E2D54")

    turtle1.shape("turtle")
    turtle1.speed(100)
    for i in range(0,36):
        draw_triangle()
        turtle1.left(10)

def draw_triangle():
    for i in range(0,3):
        turtle1.forward(100)
        turtle1.right(120)

draw_flower()
window.exitonclick()
