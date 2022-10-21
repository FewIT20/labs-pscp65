"""IG: few.pz"""
def main():
    """ Main function """
    maps = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    value = input()
    result = 0
    for i, j in enumerate(value):
        if (i + 1) == len(value) or maps[j] >= maps[value[i+1]]:
            result += maps[j]
        else:
            result -= maps[j]
    print(result)
main()
