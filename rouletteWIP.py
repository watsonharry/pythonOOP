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
        return self.name + " (" + str(self.odds) + ")"

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

class Bin(set):
    "An object used to represent the bins of a roulette wheel"
    pass

class Wheel(object):
    "An object used to represent a roulette wheel"

    def __init__(self):
        "Sets up a tuple of empty bins (ordered, immutable)"
        self.bins = tuple( Bin() for i in range(38) )
        self.seed = 1234

    def addOutcome(self,number,outcome):
        "Adds given outcome to given bin"
        self.bins[number].add(outcome)

    def next(self):
        "Generates a random number to select a bin index"
        number = rnd.randint(0,37)
        return self.getBin(number)

    def getBin(self,number):
        "Returns given bin from wheel's collection"
        return self.bins[number]
    
class BinBuilder(object):
    "An object used to algorithmically construct each of the wheel's bins"

    def populate(self,wheel):
        "Runs each of the algorithms which populate the given wheel"
        self.straight(wheel)
        self.split(wheel)

    def straight(self,wheel):
        "Generate straight bet outcomes"
        for n in range(0,36):
            "Straight bets on all of the bins whose names match their wheel indices"
            wheel.bins[n].add(Outcome("Number "+str(n),35))
        wheel.bins[37].add(Outcome("Number 00",35))

    def split(self,wheel):
        "Generate split bet outcomes"
        
        "'Vertical' split bets"
        for n in range(1,33):
            wheel.bins[n].add(Outcome(str(n)+"-"+str(n+3)+" split",17))
            wheel.bins[n+3].add(Outcome(str(n)+"-"+str(n+3)+" split",17))
        wheel.bins[0].add(Outcome("0-1 split",17))
        wheel.bins[1].add(Outcome("0-1 split",17))
        wheel.bins[3].add(Outcome("00-3 split",17))
        wheel.bins[37].add(Outcome("00-3 split",17))

        "'Horizontal' split bets"
        for r in range(0,12):
            for n in range (1,2):
                wheel.bins[n+r*3].add(Outcome(str(n+r*3)+"-"+str(n+1+r*3)+" split",17))
                wheel.bins[n+1+r*3].add(Outcome(str(n+r*3)+"-"+str(n+1+r*3)+" split",17))
        wheel.bins[0].add(Outcome("0-00 split",17))
        wheel.bins[37].add(Outcome("0-00 split",17))
            


rw = Wheel()
builder = BinBuilder()
builder.populate(rw)
print(rw.bins[28])
