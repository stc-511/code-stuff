from Card import Card
from random import randint
from codestuf import swap

class Deck():
    def __init__(self):
        self.listofcards = []
        for i in range(13):
            self.listofcards.append(Card("Spades", i + 1))
            self.listofcards.append(Card("Clubs", i + 1))
            self.listofcards.append(Card("Hearts", i + 1))
            self.listofcards.append(Card("Diamonds", i + 1))
    def printdeck(self):
        for i in range(len(self.listofcards)):
            print(self.listofcards[i].__str__() + ", ", end = "")
    def draw(self):
        return self.listofcards.pop()
    def shuffle(self):
        for i in range (104):
            swap(self.listofcards, randint(0, len(self.listofcards)-1), randint(0, len(self.listofcards)-1))
    def tellusdasizpls(self):
        return len(self.listofcards)

