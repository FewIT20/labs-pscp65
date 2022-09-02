"""IG: few.pz"""
def compare_number(value_1, value_2):
    """Compare number"""
    if value_1 > value_2:
        return value_1
    return value_2

def main():
    """Main function"""
    x_val = input()
    y_val = input()
    z_val = input()

    lastest = x_val + y_val + z_val
    lastest = compare_number((x_val + z_val + y_val), lastest)
    lastest = compare_number((y_val + x_val + z_val), lastest)
    lastest = compare_number((y_val + z_val + x_val), lastest)
    lastest = compare_number((z_val + y_val + x_val), lastest)
    lastest = compare_number((z_val + x_val + y_val), lastest)
    print(int(lastest))
main()
