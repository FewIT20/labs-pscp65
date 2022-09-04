"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for _ in range(1, value + 1):
        for row in range(1, value + 1):
            print("%d" % row, end=" ")
        print()
main()
