import turtle, random

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def tree(branchLen,t):
    if branchLen > 5:  #base case
        t.forward(branchLen)
        t.right(20)     # the turtle turns to the right by 20 degrees
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
        
def modifiedTree(branchLen,t):
    if branchLen >= 1:  #base case
        if branchLen > 40:
            t.pensize(6)
            t.color("brown")
        else:
            t.pensize(3)
            t.color("darkgreen")
        angle = random.randint(15,45)
        leafLen = random.randint(1,25)
        t.forward(branchLen)
        t.right(angle)
        modifiedTree(branchLen-leafLen,t)
        t.left(2*angle)
        modifiedTree(branchLen-leafLen,t)
        t.right(angle)
        t.backward(branchLen)
        
# TODO: Using the turtle graphics module, write a recursive program to display a Hilbert curve.
# TODO: Using the turtle graphics module, write a recursive program to display a Koch snowflake.

if __name__ == "__main__":
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    
#    drawSpiral(myTurtle,100)
#    myWin.exitonclick()

    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    myTurtle.speed(0)
    modifiedTree(75,myTurtle)
    myWin.exitonclick()

