"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    row = int(input())
    for i in range(1, value + 1):
        print(" "*(value-i), end="")
        print("*"*(i*2-1))
    for _ in range(row):
        print(" "*(value-2), end="")
        print("---")
main()
