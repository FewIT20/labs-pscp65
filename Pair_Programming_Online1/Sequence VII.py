"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for line in range(1, value+1):
        for row in range(line):
            print(row+1, end=" ")
        print()
    for line in range(value-1, 0, -1):
        for row in range(line):
            print(row+1, end=" ")
        print()
main()
