"""IG: few.pz"""
def compare_integer(var_a, var_b):
    """Find the maximum value"""
    if var_a >= var_b:
        return var_a
    else:
        return var_b

def main():
    """Main function"""
    x_val = int(input())
    y_val = int(input())

    total = compare_integer(x_val, y_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    z_val = int(input())
    total = compare_integer(total, z_val)
    print(total)
main()
