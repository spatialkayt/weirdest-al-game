from random import shuffle
from card import Card

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            print("{} - {}".format(card.suit, card.value))

    def shuffle(self):
        shuffle(self.cards)