"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    half = value //2
    for i in range(value):
        for j in range(value):
            if i == half or i + j == half or j - i == half or i - j == half or\
                 j == value - i + half - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
