"""
Blackjack game
OOP exercise
"""

import random, sys

class Card(object):
    
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    @property
    def value(self):
        v = Card.RANKS.index(self.rank) + 1
        if v > 10:
            v = 10
        return v

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep+= str(card) + " "
        else:
            rep = "<empty>"
        return rep

    @property
    def value(self):
        v = 0
        ace = 0
        for card in self.cards:
            v += card.value
            if card.value == 1:
                ace += 1
                v += 10
        while v > 21 and ace > 0:
            v -= 10
            ace -= 1
        return v
        

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,other_hand,card):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
                
    def shuffle(self):
        random.shuffle(self.cards)


"""MAIN"""

choice = None
value = 0

deck = Deck()
deck.populate()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

deck.give(player_hand,deck.cards[0])
deck.give(dealer_hand,deck.cards[0])

deck.give(player_hand,deck.cards[0])
deck.give(dealer_hand,deck.cards[0])

print("""
=========
BLACKJACK
=========
""")

value = 0
while choice != "1" and value <= 21:
    print("\nYour current hand:")
    print(player_hand)
    print("\n")
    print("1 Stick")
    print("2 Hit me")
    choice = input("Choice: ")
    if choice == "2":
        deck.give(player_hand,deck.cards[0])
        value = player_hand.value
    elif choice != "1":
        print("\nSorry, "+choice+" is not a valid choice.")

if value > 21:
    print("\nOh no! You busted! Your final hand was:")
    print(player_hand)
    sys.exit()

print("\nStuck...")

value = dealer_hand.value
while value < 17:
    deck.give(dealer_hand,deck.cards[0])
    value = dealer_hand.value

if player_hand.value > dealer_hand.value or dealer_hand.value > 21:
    print("\nCongratulations! You win.\n")
    print("\nYour hand:")
    print(player_hand)
    print("Value: ",player_hand.value)
    print("\nDealer's hand:")
    print(dealer_hand)
    print("Value: ",dealer_hand.value)

else:
    print("""\nYou're busted.\n""")
    print("\nYour hand:")
    print(player_hand)
    print("Value: ",player_hand.value)
    print("\nDealer's hand:")
    print(dealer_hand)
    print("Value: ",dealer_hand.value)        
