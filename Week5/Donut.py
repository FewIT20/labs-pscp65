"""IG: few.pz"""
def main():
    """Main function"""
    price = int(input())
    amount = int(input())
    free = int(input())
    want = int(input())
    donut = 0

    promotion = amount+free
    in_want = want // promotion
    if want == 0:
        print("0 0")
    if want > 0:
        donut = in_want*promotion
        total_left = want - donut
        if total_left > amount:
            total_left = amount
        if total_left >= amount:
            donut += promotion
        else:
            donut += total_left
        print("%d %d" % ((price*in_want*amount)+(total_left*price), donut))
main()
