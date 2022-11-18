"""IG: few.pz"""
def main():
    """ Main function """
    promotion = int(input())
    must_paid = int(input())
    standard_price = int(input())
    people = int(input())

    price = (people // promotion) * must_paid * standard_price
    price += (people % promotion) * standard_price
    print(price)
main()
