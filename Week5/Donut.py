"""IG: few.pz"""
def main():
    """Main function"""
    price = int(input())
    amount = int(input())
    free = int(input())
    want = int(input())

    in_want = want // (amount + free)
    if want == 0:
        print("0 0")
    elif want > 0:
        donut = in_want*(amount + free)
        total_left = want - donut
        if total_left > amount:
            total_left = amount
        if total_left >= amount:
            donut = donut + (amount + free)
        else:
            donut = donut + total_left
        
        total_price = (price*in_want*amount) + (total_left*price);
        print("%d %d" % (total_price, donut))
main()
