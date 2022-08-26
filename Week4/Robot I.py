"""IG: few.pz"""
 
 
def main():
    """Main function"""
    name = input()
    x_val = float(input())
    if x_val < 18:
        print("%s, you can pass." % name)
    elif x_val >= 18:
        print("%s, you shall not pass." % name)
 
 
main()
