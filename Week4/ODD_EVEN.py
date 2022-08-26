"""IG: few.pz"""
 
 
def is_odd(x_val):
    """check is odd right functions"""
    if (x_val % 2) == 0:
        return "False"
    else:
        return "True"
 
 
def main():
    """Main function"""
    print(is_odd(int(input())))
 
 
main()
