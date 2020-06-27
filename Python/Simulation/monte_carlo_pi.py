from random import random

def main():
    n = eval(input("How many darts should I throw? "))
    h = 0

    for i in range(n):
        x, y = 2*random()-1, 2*random()-1

        if x*x + y*y <= 1:
            h += 1

    pi = 4 * (h / n)

    print("The espimation of pi based on", n, "dart throws is...", pi)

main()