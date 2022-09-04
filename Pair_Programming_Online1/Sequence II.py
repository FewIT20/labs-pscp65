"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    total = 0
    i = 1
    while i <= value:
        total += (i * 2 - 1)
        print(total, end=" ")
        i = i + 1
main()
