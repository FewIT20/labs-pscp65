"""IG: few.pz"""
def main():
    """Main function"""
    gcd = int(input())
    value = int(input())
    while value != 0:
        gcd, value = value, gcd % value
    print(gcd)
main()
