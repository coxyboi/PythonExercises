from random import randrange

def roll():
    return randrange(1,7) + randrange(1,7)

def winMsg():
    print("You win, faggot")

def loseMsg():
    print("You lose, cuckold")

def rollLoop(initial):
    newRoll = 0
    
    while newRoll != initial and newRoll != 7:
        newRoll = roll()
        print("New Roll:", newRoll)
        if newRoll == 7:
            loseMsg()
            return(False)
        elif newRoll == initial:
            winMsg()
            return(True)

def playGame():
    initial = roll()
    print("Initial:", initial)

    winCondition = initial == 7 or initial == 11
    loseCondition = initial == 2 or initial == 3 or initial == 12

    if winCondition:
        winMsg()
        return True
    elif loseCondition:
        loseMsg()
        return False
    else:
        decision = rollLoop(initial)
        return decision

def playNGames():
    n = eval(input("How many games should i simulate, papi? "))
    winCount = 0

    for i in range(n):
        if playGame():
            winCount += 1
            print("Won")
            print("-------------------------------------")
        else:
            print("Lost")
            print("-------------------------------------")

    print("\nThe probability of winning", n, "games is", winCount, "/", n)

def main():
    playNGames()

main()