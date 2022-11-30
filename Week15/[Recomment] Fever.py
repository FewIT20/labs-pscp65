"""IG: few.pz"""
def main():
    """ Main function """
    fever = float(input())
    if 36 <= fever < 38:
        print("No Fever")
    elif 38 <= fever < 39:
        print("Mild Fever")
    elif 39 <= fever < 40:
        print("High Fever")
    else:
        print("Very High Fever")
main()
