"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for line in range(1, value+1):
        for _ in range(value-line):
            print("  ", end=" ")
        for row in range(1, line + 1):
            print("%02d" %row, end=" ")
        print()
main()
