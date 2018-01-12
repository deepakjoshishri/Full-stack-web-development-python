import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.fillcolor("blue")
    brad.speed(1000000000000)
    for j in range(0,72):
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.left(5)
    

draw_square()
window.exitonclick()
