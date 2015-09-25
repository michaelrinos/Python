from math import modf

"""
Author: Michael Rinos
"""


bills = [20, 10, 5, 1]
coins = [.25, .10, .05, .01]
paperChange = [0, 0, 0, 0]
coinChange = [0, 0, 0, 0]

def main():
    total = float(input("Enter the total due: "))
    amount = float(input("Enter the amount given: "))
    Calculate(total, amount)

def Calculate(total, amount):
    x = amount%total
    for w in bills:
        if x//w>0:
            paperChange.insert(bills.index(w),x//w)
            paperChange.pop(bills.index(w)+1)

    for w in coins:
        if x//w>0:
            coinChange.insert(coins.index(w),x//w)
            coinChange.pop(coins.index(w)+1)

    
    print(paperChange)
    
    

main()
