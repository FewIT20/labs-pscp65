"""IG: few.pz"""
def main():
    """ Main function """
    count = input()
    if count[-1] == "3" or int(count) % 3 == 0:
        print("PONG")
    else:
        print(count)
main()
