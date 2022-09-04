"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for line in range(0, value):
        for row in range(value):
            print(2 + line + row, end=" ")
        print()
main()
