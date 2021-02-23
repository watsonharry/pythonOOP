"""
Dice problem

For two collections of dice, if possible, what is the
smallest number of dice that can be turned to make the sum
values of both collections equal?
"""

import random as rnd

class dicepool(object):
    "An object to represent a pool of dice"

    def __init__(self,size):
        self.size = size
        self.dice = [0 for x in range(size)]
        self.populate()

    def __str__(self):
        return str(self.dice)

    def populate(self):
        for n in range(0,self.size):
            self.dice[n] = rnd.randint(1,6)

    def sum(self):
        result = 0
        for n in range(0,self.size):
            result += self.dice[n]
        return result

    def length(self):
        "Returns the length of the array"
        return self.size

class sorter(object):
    "An object to contain the pools and functions required to solve the problem"

    def __init__(self):
        self.pot = -1
        "self.pot contains the index of the pool with most potential (see func)"
        self.pools = []

    def __str__(self):
        if self.pools:
            rep = ""
            for pool in self.pools:
                rep += str(pool) + "\n"
        else:
            rep = "<empty>"
        return rep

    def populate(self,size1,size2):
        self.pools.append(dicepool(size1))
        self.pools.append(dicepool(size2))

    def potential(self,dp1,dp2):
        """
        Determines which dice pool is most polarised, i.e. has the most
        high/low values and the least 'middle of the road' ones. This dice
        pool has the most 'potential' for higher sum value change with fewer
        dice turns.
        """

        pot1 = abs(3.5 * dp1.length() - dp1.sum())
        print(str(pot1))
        pot2 = abs(3.5 * dp2.length() - dp2.sum())
        print(str(pot2))

        if pot1 > pot2:
            return 0
        else:
            return 1

    def possible(self,dp1,dp2):
        """
        Checks whether it's possible for these two dice pools to have the same
        value, by checking if their ranges of possible sums overlap.
        """

        L1 = dp1.length()
        L2 = dp2.length()
        L_max = max(L1,L2)
        L_min = L1+L2 - L_max
        return 6*L_min - L_max >= 0


    def solve(self,dp1,dp2):
        poss = self.possible(dp1,dp2)
        if pos == 0:
            print("\nThese two pools cannot share the same sum value.")
        else:
            self.pot = self.potential()
        


sort = sorter()
sort.populate(8,7)
print(sort)
print(str(sort.possible(sort.pools[0],sort.pools[1])))
sort.potenital(sort.pools[0],sort.pools[1]))
