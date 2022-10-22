"""IG: few.pz"""
import math

def main():
    """ Main function """
    grow, count = [int(x) for x in input().split()]

    areas = []
    for _ in range(count):
        posx, posy = [int(x) for x in input().split()]
        result = (posx ** 2 + posy ** 2) ** 0.5
        result = 3.1416 * result ** 2
        areas.append(result)

    for area in areas:
        print(math.ceil(area/grow))
main()
