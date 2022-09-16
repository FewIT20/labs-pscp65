"""IG: few.pz"""
def main():
    """Main function"""
    length_val = int(input())
    a_val = int(input())
    b_val = int(input())
    c_val = int(input())
    d_val = int(input())
    stamp = 0
    total = 0
    for _ in range(length_val):
        amount = int(input())
        discount = amount
        while True:
            if stamp >= c_val and discount > 0:
                stamp -= c_val
                discount -= d_val
            else:
                break
        if amount >= a_val:
            if b_val != 0 or d_val != 0:
                stamp += int((discount / a_val)) * b_val
        if discount <= 0:
            total += 0
        else:
            total += discount
    print("%d" % total)
    print("%d" % stamp)
main()
