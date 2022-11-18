"""IG: few.pz"""
def main():
    """ Main function """
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    for i in range(num1, 0, -1):
        for j in range(i, (num1 * num2) + 1, num1):
            if j == num3:
                print("XX", end=" ")
            else:
                print("%0.2d" % (j), end=" ")
        if i % 2 != 0 and i != 1:
            print()
        print()
main()
