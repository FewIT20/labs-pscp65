"""IG: few.pz"""
def digit_sum(x_val):
    """Sum of digits"""
    value = 0
    x_val = str(x_val)
    if int(x_val) < 0:
        for i in x_val[1:]:
            value = value + int(i)
        value = value * (-1)
    else:
        for i in x_val:
            value = value + int(i)
    return value

def main():
    """Main function"""
    for _ in range(10):
        x_val = int(input())
        # If input is 0, then say NO!
        if x_val == 0:
            print("No")
        elif len(str(x_val)) == 1:
            # If input is same input, then say YES!
            if x_val % x_val == 0:
                print("Yes")
            else:
                print("No")
        else:
            # Process the input
            if x_val % digit_sum(x_val) == 0:
                print("Yes")
            else:
                print("No")
main()
