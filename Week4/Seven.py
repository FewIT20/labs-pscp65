"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    if value % 4 == 1:
        print("7")
    elif value % 4 == 2:
        print("9")
    elif value % 4 == 3:
        print("3")
    elif value % 4 == 0:
        print("1")
main()
