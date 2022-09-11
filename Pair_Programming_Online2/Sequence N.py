"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for i in range(value):
        for j in range(value):
            if i == j or j == value - 1 or j == 0:
                print("*", end="")
            else:
                print("", end=" ")
        print()
main()
