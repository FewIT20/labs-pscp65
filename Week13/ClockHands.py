"""IG: few.pz"""
def main():
    """ Main function """
    hour = int(input())
    seconds = int(input())
    hour *= 5
    hour += seconds / 12
    hour %= 60
    print(seconds <= hour < seconds+1)
main()
