from Deck import Deck

deckocards = Deck()
deckocards.shuffle()
player = []
playerscore = 0
house = []
housescore = 0
for i in range(2):
    player.append(deckocards.draw())
    house.append(deckocards.draw())
def printlist(list):
        for i in range(len(list)):
            print("You have a(n)", list[i], ",")
def pointchecker(deck):
    aces = 0
    score = 0
    for i in range(len(deck)):
        if deck[i].value > 1 and deck[i].value < 11:
            score += deck[i].value
        elif deck[i].value > 10:
            score += 10
        elif deck[i].value == 1:
            score += 1
            aces += 1
    for o in range(aces):
        if score < 12:
            score += 10
    return score
while playerscore < 22 or housescore < 22:
    printlist(player)
    print("The house has a(n)", house[0])

    while True:
        print("Your cards are,")
        printlist(player)
        hit = input("Hit 'enter' to hit and type 'stand' to stand")
        playerscore = pointchecker(player)
        print("Your score is", playerscore)
        if hit == "":
            player.append(deckocards.draw())
        if hit == "stand" or pointchecker(playerscore) > 20:
            break
    while pointchecker(house) < 17:
        housescore = pointchecker(house)
        print("The houses score is", housescore)
        house.append(deckocards.draw())
    break
print("Players score is", pointchecker(player))
print("Houses score is", pointchecker(house))
print("You can do math who won.")