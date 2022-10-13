"""IG: few.pz"""
def main():
    """Main function"""
    gcd = int(input())
    value = int(input())
    for i in range(100000, 0, -1):
        if gcd % i == 0 and value % i == 0:
            print(i)
            break
main()
