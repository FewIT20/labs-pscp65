"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for i in range(1, value+1):
        for j in range(-value+1, value, 1):
            if j == 0 or abs(j) < i:
                print("%02d" % (i-abs(j)), end=" ")
            else:
                print("  ", end=" ")
        print()
main()
