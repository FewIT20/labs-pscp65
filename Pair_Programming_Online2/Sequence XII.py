"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for i in range(-value + 1, value):
        for j in range(-value + 1, value):
            print("%02d"%(value - abs(abs(i) - abs(j))), end=" ")
        print()
main()
