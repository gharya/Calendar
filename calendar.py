# -*- coding: utf-8 -*-
"""
Functions about calendars

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 1

def gregorian(year):
    if year % 4 == 0:
        print(f'gregorian({year}) = ', True)
        return True
    print(f'gregorian({year}) ', False)
    return False


def milankovic(year):
    if year%4==0 and year%100!=0:
        print(f"milankovic({year}) = ", True)
        return True
    print(f"milankovic({year}) = ", False)
    return False


def gregorian_count(year1, year2):
    count = 0
    for year in range(year1,year2):
        if year%4==0 and (year%100!=0 or year%400==0):
            count+=1
    print(f"gregorian_count({year1}, {year2}) count is => ",count)
    return count
    


def milankovic_count(year1, year2):
    count = 0
    for year in range(year1,year2):
        if year%4==0:
            if year%100!=0 or year%900==400 or year%900==600:
                count+=1
    print(f"milankovic_count({year1}, {year2}) count is => ",count)
    return count



def main():
    test1()
    test2()
    testN()


###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for gregorian()
def test1():
    print(" Test case 1 ")
    gregorian(1696)
    milankovic(1696)
    gregorian_count(1696,1697)
    milankovic_count(1696,1697)
    print()

def test2():
    print(" Test case 2 ")
    gregorian(1697)
    milankovic(1697)
    gregorian_count(1900,1901)
    milankovic_count(1900,1901)
    print()

# Below are the tests for milankovic()
def testN():
    print(" Test case 3 ")
    gregorian(2100)
    milankovic(2100)
    gregorian_count(2000,3000)
    milankovic_count(2000,300)
    print()

    
###############################################################    
    
if __name__ == "__main__":
    main()    