"""IG: few.pz"""
def main():
    """Main function"""
    size = int(input())
    unit = int(input())
    for i in range(size):
        if i == 0 or i == size-1:
            for _ in range(unit):
                print("*" * size, end=" ")
            print()
        else:
            for _ in range(unit):
                for j in range(size):
                    if i == j or j == 0 or j == size-1 or j == size-1-i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()
main()
