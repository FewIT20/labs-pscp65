"""IG: few.pz"""
def main():
    """Main function"""
    order = input()

    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    if order.lower() == "ascend":
        print("%.2f, %.2f, %.2f " %(num1, num2, num3))
    elif order.lower() == "descend":
        print("%.2f, %.2f, %.2f " %(num3, num2, num1))

main()
