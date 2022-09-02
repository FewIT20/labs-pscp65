"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for i in range(1, value+1):
        if i == value:
            print(i, end="")
        else:
            print(i, end="_")
main()
