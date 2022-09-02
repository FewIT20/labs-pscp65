"""IG: few.pz"""
def main():
    """Main function"""
    x_val = float(input())
    y_val = float(input())

    #Define defualt 0
    z_val = 0
    if y_val*2 < x_val:
        z_val = x_val-y_val*2
    if y_val - z_val > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
