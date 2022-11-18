"""IG: few.pz"""


def main():
    """ Main function """
    name, num = input(), int(input())
    if (name == "Kids" and num < 11) or (name == "Adults" and num < 26):
        print("Very Slow")
    elif name == "Kids":
        if 11 <= num <= 20:
            print("Slow")
        elif num <= 30:
            print("Average")
        elif num <= 40:
            print("Fast")
        else:
            print("Very Fast")
    elif name == "Adults":
        if 26 <= num <= 35:
            print("Slow/Beginner")
        elif num <= 45:
            print("Intermediate/Average")
        elif num <= 65:
            print("Fast/Advanced")
        elif num <= 80:
            print("Very Fast")
        else:
            print("Insane")


main()
