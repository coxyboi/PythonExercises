from graphics import *
from button import Button
from random import randrange

def winMsg(win, msgObj):
    msgObj.undraw()
    msgObj.setText("You won.")
    msgObj.draw(win)

def loseMsg(win, msgObj):
    msgObj.undraw()
    msgObj.setText("You lost.")
    msgObj.draw(win)

def main():
    win = GraphWin("Monty Hall", 800, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("cyan1")

    # draw text
    msg = Text(Point(5,8), "We are never getting to mars.")
    msg.setSize(30)
    msg.setFace("helvetica")
    msg.setStyle("bold")
    msg.setTextColor("pink3")
    msg.draw(win)

    # setup buttons
    b1 = Button(win, Point(3,3), 1, 0.5, "Door 1")
    b2 = Button(win, Point(5,3), 1, 0.5, "Door 2")
    b3 = Button(win, Point(7,3), 1, 0.5, "Door 3")
    b1.activate()
    b2.activate()
    b3.activate()

    done = False
    choice = randrange(1,4)

    while not(done):
        p = win.getMouse()
        if choice == 1 and b1.clicked(p):
            winMsg(win, msg)
        elif choice == 2 and b2.clicked(p):
            winMsg(win, msg)
        elif choice == 3 and b3.clicked(p):
            winMsg(win, msg)
        elif choice != 1 and b1.clicked(p):
            loseMsg(win, msg)
        elif choice != 2 and b2.clicked(p):
            loseMsg(win, msg)
        elif choice != 3 and b3.clicked(p):
            loseMsg(win,msg)
        else: #not(b1.clicked(p) or b2.clicked(p) or b3.clicked(p)):
            msg.undraw()
            msg.setText("No button licked")
            msg.draw(win)


main()