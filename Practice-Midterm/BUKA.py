"""IG: few.pz"""
def main():
    """Main function"""
    x_value = int(input())
    operator = input()
    y_value = int(input())
    if operator == "+":
        print("%d" % (x_value + y_value))
    elif operator == "*":
        print("%d" % (x_value * y_value))
main()
