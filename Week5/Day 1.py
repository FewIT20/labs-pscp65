"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    if (value % 400 == 0) or (value % 100 != 0) and (value % 4 == 0):
        print("Yes")
    else:
        print("No")
main()
