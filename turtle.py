import turtle

p = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(p, lineLen):
    if lineLen > 0:
        p.forward(lineLen)
        p.right(90)

        drawspiral(p, linLen - 5)

drawSpiral(p, 100)
myWin.exitonclick()
