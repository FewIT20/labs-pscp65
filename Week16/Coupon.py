"""IG: few.pz"""
def main():
    """ Main function """
    price, coupon1, coupon2 = float(input()), input(), input()
    discount_1, mincost_1 = [float(i) for i in coupon1.split()]
    discount_2, mincost_2 = [float(i) for i in coupon2.split()]
    price_cp1 = price_cp2 = price

    if price >= mincost_1:
        price_cp1 = max(0, price - discount_1)
    if price >= mincost_2:
        price_cp2 = max(0, price*(100-discount_2)/100)

    if price_cp1 == price_cp2 == price:
        print("Nope")
    elif price_cp1 == price_cp2:
        print("1" if mincost_1 <= mincost_2 else "2", "%.1f" % price_cp1)
    elif price_cp1 < price_cp2:
        print("1 %.1f "% price_cp1)
    else:
        print("2 %.1f" % price_cp2)
main()
