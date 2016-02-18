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
    print("%.2f"%(amount%total))

main()
