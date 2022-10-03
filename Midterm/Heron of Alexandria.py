"""IG: few.pz"""
def calculate_formula_s(x_value, y_value, z_value):
    """Calculate formula s"""
    return (x_value + y_value + z_value) / 2

def main():
    """Main function"""
    x_value, y_value, z_value = float(input()), float(input()), float(input())
    s_value = calculate_formula_s(x_value, y_value, z_value)
    area = (s_value*((s_value-x_value)*(s_value-y_value)*(s_value-z_value)))**0.5
    print("%.3f" % area)
main()
