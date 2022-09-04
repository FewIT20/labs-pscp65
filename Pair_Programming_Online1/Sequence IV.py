"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    attempted = value
    col = 0
    for _ in range(0, value):
        for i in range(col, value):
            print(i + 1, end=" ")
            col = i + 1
        value = value + attempted
        print("")
main()
