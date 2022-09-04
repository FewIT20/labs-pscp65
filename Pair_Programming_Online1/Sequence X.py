"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    for row in range(-(value-1), value):
        for col in range(-(value-1), value):
            if value - abs(row) >= abs(col) +1:
                print("%02d" % (value-abs(col) -abs(row)), end=" ")
            else:
                print("  ", end=" ")
        print()
main()
