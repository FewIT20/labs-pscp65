"""IG: few.pz"""
def is_odd(x_val):
    """Check is odd function"""
    if (x_val % 2) == 0:
        return "False"
    else:
        return "True"
 
def main():
    """Main function"""
    print(is_odd(int(input())))
 
 
main()
