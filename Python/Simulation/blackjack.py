from random import randrange

def drawACard():
    # 16 tens, 4 nines, 4 eights, etc. 4 aces
    deckOfCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10]
    index = randrange(1, 14)
    return deckOfCards[index-1]

def playGame():
    dealerTotal = 0
    playerTotal = 0
    dealerHasAce = False
    playerHasAce = False

    while dealerTotal <= 21 and playerTotal <= 21:
        # dealer's turn
        newDealerCard = drawACard()

        if newDealerCard == 1:
            dealerHasAce = True
            print("Dealer has drawn an ace")

        if dealerHasAce and (dealerTotal+10 >= 17 and dealerTotal+10 <= 21):
            dealerTotal += 10

        if dealerTotal >= 21:
            print("The dealer has won.")

        dealerTotal += newDealerCard

        # player's turn
        newPlayerCard = drawACard()
        
        if newPlayerCard == 1:
            playerHasAce = True
            print("Player has drawn an ace")

        if playerHasAce and (playerTotal+10 >= 17 and playerTotal+10 <= 21):
            playerTotal += 10

        if playerTotal >= 21:
            print("The player has won.")

        playerTotal += newPlayerCard

        # display current totals
        print(dealerTotal, playerTotal)

def main():
    playGame()

main()