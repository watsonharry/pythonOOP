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

    def next(self):
        "Generates a random number to select a bin index"
        number = rnd.randint(0,37)
        return self.getBin(number)

    def getBin(self,number):
        "Returns given bin from wheel's collection"
        return self.bins[number]

    def debug(self):
        "Prints the outcomes of each bin. Used to test whether a wheel has been"
        "constructed correctly"
        for n in range(0,38):
            print("Index: "+str(n))
            print(self.getBin(n))
            print("")
    
class BinBuilder(object):
    "An object used to algorithmically construct each of the wheel's bins"

    def populate(self,wheel):
        "Runs each of the algorithms which populate the given wheel"
        self.straight(wheel)
        self.split(wheel)
        self.street(wheel)
        self.corner(wheel)
        self.column(wheel)
        self.line(wheel)
        self.dozen(wheel)
        self.colour(wheel)
        self.parity(wheel)
        self.hilo(wheel)

    def straight(self,wheel):
        "Generate straight bet outcomes"
        for n in range(0,37):
            "Straight bets on all of the bins whose names match their wheel indices"
            wheel.bins[n].add(Outcome("Number "+str(n),35))
            
        wheel.bins[37].add(Outcome("Number 00",35))

    def split(self,wheel):
        "Generate split bet outcomes"
        
        "'Vertical' split bets"
        for n in range(1,34):
            outcome = Outcome(str(n)+"-"+str(n+3)+" split",17)
            wheel.bins[n].add(outcome)
            wheel.bins[n+3].add(outcome)
            
        wheel.bins[0].add(Outcome("0-1 split",17))
        wheel.bins[1].add(Outcome("0-1 split",17))
        wheel.bins[3].add(Outcome("00-3 split",17))
        wheel.bins[37].add(Outcome("00-3 split",17))

        "'Horizontal' split bets"
        for r in range(0,12):
            for n in range (1,3):
                outcome = Outcome(str(n+r*3)+"-"+str(n+1+r*3)+" split",17)
                wheel.bins[n+r*3].add(outcome)
                wheel.bins[n+1+r*3].add(outcome)
                
        wheel.bins[0].add(Outcome("0-00 split",17))
        wheel.bins[37].add(Outcome("0-00 split",17))

    def street(self,wheel):
        "Generate street bet outcomes"
        for r in range(0,12):
            for n in range(1,4):
                outcome = Outcome(str(1+r*3)+"-"+str(2+r*3)+"-"+str(3+r*3)+" street",11)
                wheel.bins[n+r*3].add(outcome)
                
        outcome = Outcome("0-1-2-3-00 street",6)
        for n in range(0,4):
            wheel.bins[n].add(outcome)
        wheel.bins[37].add(outcome)

    def corner(self,wheel):
        "Generate corner bet outcomes"
        for r in range(0,11):
            for n in range(1,3):
                outcome = Outcome(str(n+r*3)+"-"+str(n+1+r*3)+"-"+str(n+3+r*3)+"-"+str(n+4+r*3)+" corner",8)
                wheel.bins[n+r*3].add(outcome)
                wheel.bins[n+1+r*3].add(outcome)
                wheel.bins[n+3+r*3].add(outcome)
                wheel.bins[n+4+r*3].add(outcome)
                
        outcome = Outcome("0-1-2 corner",11)
        for n in range(0,3):
            wheel.bins[n].add(outcome)
            
        outcome = Outcome("2-3-00 corner",11)
        for n in range(2,4):
            wheel.bins[n].add(outcome)
        wheel.bins[37].add(outcome)
        
        outcome = Outcome("0-2-00 corner",11)
        wheel.bins[0].add(outcome)
        wheel.bins[2].add(outcome)
        wheel.bins[37].add(outcome)

    def line(self,wheel):
        "Generate line bet outcomes"
        for r in range(0,11):
            outcome = Outcome(str(1+r*3)+"->"+str(6+r*3)+" line",5)
            for n in range(1,4):
                wheel.bins[n+r*3].add(outcome)
                wheel.bins[n+3+r*3].add(outcome)

    def dozen(self,wheel):
        "Generate dozen bets"
        for r in range(0,3):
            outcome = Outcome(str(1+r*12)+"->"+str(12+r*12)+" dozen",2)
            for n in range(1,13):
                wheel.bins[n+r*12].add(outcome)
        
    def column(self,wheel):
        "Generate column bet outcomes"
        for r in range(1,4):
            for n in range(0,12):
                wheel.bins[r+n*3].add(Outcome("Column "+str(r),2))

    def colour(self,wheel):
        "Generate red bet outcomes"
        outcome = Outcome("red",1)
        pattern = [0,2,2,2,2,3,2,2,2,1,2,2,2,2,3,2,2,2]
        "^This is the pattern of distances between red bins"
        for n in range(0,len(pattern)+1):
            wheel.bins[1+sum(pattern[0:n])].add(outcome)
            
        "Generate black bet outcomes"
        outcome = Outcome("black",1)
        pattern = [1,2,2,2,2,1,2,2,2,3,2,2,2,2,1,2,2,2]
        for n in range(0,len(pattern)+1):
            wheel.bins[1+sum(pattern[0:n])].add(outcome)

    def parity(self,wheel):
        "Generate odd outcomes"
        outcome = Outcome("odd",1)
        for n in range(0,18):
            wheel.bins[1+n*2].add(outcome)
            
        "Generate even outcomes"
        outcome = Outcome("even",1)
        for n in range(0,18):
            wheel.bins[2+n*2].add(outcome)

    def hilo(self,wheel):
        "Generates high/low outcomes"
        outcome = Outcome("low",1)
        for n in range(1,19):
            wheel.bins[n].add(outcome)
            
        outcome = Outcome("high",1)
        for n in range(19,37):
            wheel.bins[n].add(outcome)
        
rw = Wheel()
builder = BinBuilder()
builder.populate(rw)
rw.debug()
