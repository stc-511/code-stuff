from Deck import Deck

deck = Deck()
deck.shuffle()
playerscore = 0 
computerscore = 0
while deck.tellusdasizpls() > 0:
    playercard = deck.draw()
    computercard = deck.draw()
    print("Player card is,", playercard)
    print("Computer card is,", computercard)
    if playercard.value > computercard.value:
        print("Player wins")
        playerscore += 1
    
    elif computercard.value > playercard.value:
        print("Computer wins")
        computerscore += 1
    else:
        tiebreakcount = 2
        while playercard.value == computercard.value:
            for i in range(4):
                if deck.tellusdasizpls() > 1:
                    playercard = deck.draw()
                    computercard = deck.draw()
                    tiebreakcount += 2
                else:
                    break
            if playercard.value> computercard.value:
                print("Player wins tiebreak")
                playerscore += tiebreakcount
            else:
                print("Computer wins tiebreak")
                computerscore += tiebreakcount
if playerscore > computerscore:
    print("Player wins like the whole game!!!!")
if playerscore < computerscore:
    print("Computer wins like the whole game!!!!")
