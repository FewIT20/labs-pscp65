"""IG: few.pz"""
def main():
    """ Main function """
    balance = int(input())
    load = float(input())
    year = int(input())
    for _ in range(year):
        balance += balance * load / 100
    print("%.2f" % balance)
main()
