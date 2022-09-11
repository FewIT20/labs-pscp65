"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for i in range(-value + 1, value, 1):
        for j in range(-value + 1, value, 1):
            if abs(i) > abs(j) - 1:
                print("%02d"%(value - abs(i)), end=" ")
            else:
                print("%02d"%(value - abs(j)), end=" ")
        print()
main()
