"""IG: few.pz"""
def main():
    """Main function"""
    row = int(input())
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
main()
