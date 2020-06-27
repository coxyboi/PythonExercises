from graphics import *
from random import random
import math
import time

def drawCircle(win, x, y):
    p = Point(x, y)
    c = Circle(p, 4)
    c.setFill("orange")
    c.setWidth(1)
    c.setOutline("cyan")
    c.draw(win)

def drawLine(win, p1, p2):
    l = Line(p1, p2)
    l.setWidth(4)
    l.setFill("purple")
    l.draw(win)

def main():
    windowX, windowY = 1920, 1080#eval(input("How big should the window be? (x, y) "))

    win = GraphWin("Random Walk", windowX, windowY)
    win.setBackground("turquoise")
    x = windowX / 2
    y = windowY / 2
    x0 = x
    y0 = y
    multiplier = 50

    for i in range(5000):
        angle = random() * 2 * math.pi
        
        x0 = x + math.cos(angle)*multiplier
        y0 = y + math.sin(angle)*multiplier

        if not(x0 > 0 and x0 < windowX):
            x0 = x
        if not(y0 > 0 and y0 < windowY):
            y0 = y

        p1 = Point(x, y)
        p2 = Point(x0, y0)
        drawCircle(win, x, y)
        drawLine(win, p1, p2)
        print(x, y)
        x = x0
        y = y0
        #time.sleep(0.000001)
        

    win.getMouse()
    win.close()

main()