class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        if self.value < 11 and self.value > 1:
            return str(self.value) + " of " + self.suit
        elif self.value == 1:
            return("Ace of " + self.suit)
        elif self.value == 11:
            return("Jack of " + self.suit)
        elif self.value == 12:
            return("Queen of " + self.suit)
        elif self.value == 13:
            return("King of " + self.suit)
cheese = Card("Spades", 1)
