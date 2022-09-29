"""IG: few.pz"""

def main():
    """Main function"""
    value = input().split()
    x_val = float(value[0])
    y_val = float(value[1])
    
    print("%.6f" % (x_val**2 + y_val**2)**0.5)
main()
