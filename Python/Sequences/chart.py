# i worked way too hard on this


from graphics import *

def main():
    infileName = r"D:\Users\owenf\Desktop\Python\Sequences\exam_scores.txt"
    infile = open(infileName, "r")

    win = GraphWin("Chart", 1000, 1000)

    nameLoc = Point(50, 50)
    recPoint1 = Point(100, 40)

    for line in infile:
        nameStr = line.split()[0]
        score = int(line.split()[1])

        # draw the name
        nameTextObject = Text(nameLoc, nameStr)
        nameTextObject.draw(win)

        # draw the score bar
        recPoint2 = Point(100+score*4, recPoint1.y+10)
        bar = Rectangle(recPoint1, recPoint2)
        bar.draw(win)

        # draw the score
        scoreTextPoint = Point(120+score*4, recPoint1.y+5)
        scoreTextObject = Text(scoreTextPoint, score)
        scoreTextObject.draw(win)

        # update locations
        nameLoc.move(0, 20)
        recPoint1.move(0, 20)
    
    win.getMouse()

main()