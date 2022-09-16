"""IG: few.pz"""
def main():
    """Main function"""
    price = int(input())

    value = price * 10 / 100
    #value is less 50, set value to 50
    if value < 50:
        value = 50
    #Than value is most 1000, set value to 1000
    if value > 1000:
        value = 1000

    #Let's process it, I don't care grammar because my english so bad ;-;
    total = price + value
    total = total * 107 / 100
    print("%.2f" % total)
main()
