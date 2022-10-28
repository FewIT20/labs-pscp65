"""IG: few.pz"""
import math

def main():
    """ Main function """
    players = int(input())
    if players % 2 != 0:
        players += 1
    result = (math.factorial(players))/((math.factorial(players-(players//2))) \
        * (math.factorial(players//2)))
    print(int(result))
main()
