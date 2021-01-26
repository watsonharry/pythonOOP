"""
Roulette Game
"""

"""

BET TYPES

-Straight: single number 35:1
-Split: adjacent (on table) pair of numbers 17:1
-Street: three numbers on a single row 11:1
-Corner: square of 4 numbers 8:1
-Corner end: corner of 0,00,1,2,3 6:1
-Line: six number block i.e. two adjacent street bets 5:1
-12-number range: 2:1
-Column: 2:1
-18-number range: 1:1
-Colour bet: 1:1
-Even/odd (doesn't include 0 or 00): 1:1

"""

import random as rnd

class Outcome(object):
    "An object used to represent bets and spin results"

    def __init__(self,name,odds):
        self.name = name
        self.odds = odds

    def __str__(self):
        return self.name + " (" + self.odds + ")"

    def __repr__(self):
        """"
        Overriding __repr__ because I want to be able to easily
        print Bins (sets of outcomes)
        """
        return self.__str__()

    def winAmount(self, amount):
        "Multiplies bet by outcome's odds"
        return amount*odds
        
    def __eq__(self, other):
        "Compare the bet name attributes of self and other"
        return self.name == other.name

    def __ne__(self, other):
        "As for __eq__, but inverted result"
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

class Bin(frozenset):
    "An object used to represent the bins of a roulette wheel"

class Wheel(object):

    def __init__(self,bins,seed):
        self.bins = bins
        rnd.seed(self.seed)
        
    def addOutcome(number,outcome):
        "Adds an outcome to a bin"
        self.bins[number].append(outcome)

    def spin(self):
        return rnd.choice(self.bins)

    def get(self,number):
        return self.bins[number]

class BinBuilder(object):
    "An object used to add outcomes to each of the bins"
