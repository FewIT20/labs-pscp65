"""IG: few.pz"""
def main():
    """Main function"""
    average = float(input())
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_d = (average * 4) - (val_a+val_b+val_c)
    less = average-(average/2)
    more = average + (average/2)
    if average * 4 > 15000:
        print("Overweight")
    elif  less < val_a < more and less < val_b < more and less < val_c < more\
 and less < val_d < more:
        print("Pass %.2f"%val_d)
    else:
        print("Unbalance")
main()
