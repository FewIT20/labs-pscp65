"""IG: few.pz"""
def main():
    """Main function"""
    value = input().split()
    x_val = int(value[0])
    y_val = int(value[1])
    z_val = int(value[2])
    
    x_value = z_val - y_val - 1
    y_value = y_val - x_val - 1
    if x_value == y_value:
        print(x_value)
    elif x_value > y_value:
        print(x_value)
    elif y_value > x_value:
        print(y_value)
main()
