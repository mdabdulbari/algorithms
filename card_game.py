import random
from random import randint

class Card:

    def __init__(self, number, suit):

        self.number = number
        self.suit = suit

    def getNumber(self):

        return self.number
    
    def getSuit(self):

        return self.suit

    def __str__(self):
        return str(str(self.number) + " of " + self.suit)

class Deck:
    
    def __init__(self):
    
        self.__card_list = []
        for suit in ["clubs", "diamonds", "hearts", "spades"]:
            a = Card("A", suit)
            self.__card_list.append(a)

            for i in range(9):
                a = Card(i, suit)
                self.__card_list.append(a)
            
            for j in ["J", "Q", "K"]:
                a = Card(j, suit)
                self.__card_list.append(a)
    
    def __str__(self):
        out = ""
        for card in self.__card_list:
            out += str(card)
            out += "\n"
        return out

    def shuffle(self):
        random_number_list = []
        list1 = []
        for i in range(52):
            random_number_list.append(i) 
        for i in range(52):
            random_number = randint(0,len(self.__card_list) - 1)
            tmp_card = self.__card_list.pop(random_number)
            list1.append(tmp_card)
        self.__card_list = list1

deck = Deck()
print(deck)
deck.shuffle()
print(deck)