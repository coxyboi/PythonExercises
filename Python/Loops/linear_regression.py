from graphics import *
from math import *

# draws a linear regression line through data from data.txt

def main():
    # set up window
    win = GraphWin("1488", 1000, 1000)
    win.setCoords(0.0, 0.0, 100.0, 100.0)
    # set up file io
    infileName = r"D:\Users\owenf\Desktop\Python\Loops\data.txt"
    infile = open(infileName, "r")

    # vars for math:
    sumXY = 0
    sumXX = 0
    sumX = 0
    sumY =0
    meanY = 0
    meanX = 0
    n = 0

    for line in infile:
        # organize data
        data = line.replace("\n", "").split(", ")

        # draw data points
        p = Point(int(data[0]), int(data[1]))
        c = Circle(p, 1)
        c.setFill("teal")
        c.draw(win)

        # do vars
        sumXY += eval(data[0]) * eval(data[1])
        sumXX += eval(data[0]) * eval(data[0])
        n += 1
        sumX += eval(data[0])
        sumY += eval(data[1])

    # do math
    meanX = sumX / n
    meanY = sumY / n
    m = (sumXY - n * sumX * sumY) / (sumXX - n * sumX * sumX)
    print(m)

    # draw line
    p1 = Point(0, sumY+m*(0-sumX))
    p2 = Point(100, sumY+m*(100-sumX))
    line = Line(p1, p2)
    line.setWidth(8)
    line.setFill("purple")
    line.draw(win)

    win.getMouse()

main()