"""IG: fewpz"""
 
 
def main():
    """Main functions"""
    x_val = int(input())
    y_val = float(input())
    z_val = input()
 
    print(("%d" % x_val).rjust(30, " "))
    print(("%030d" % x_val))
    print("%.2f" % y_val)
    print("%.12f" % y_val)
    print("%40s" % z_val)
 
 
main()