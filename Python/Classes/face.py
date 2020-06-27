from graphics import *

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)

    def smile(self, window):
        p1 = Point(200, 200)
        p2 = Point(700, 400)
        self.mouth = Line(p1, p2)
        self.mouth.draw(window)

def main():
    x, y = 800, 600
    win = GraphWin("Face", x, y)
    center = Point(x/2,y/2)
    face = Face(win, center, 100)
    face.smile(win)
    win.getMouse()

main()