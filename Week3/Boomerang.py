"""IG: fewpz"""
def call_function_five(x_value, y_value, z_value):
    """Call this function calutate"""
    return (y_value - ((y_value**2) - (4*x_value*z_value))**0.5) / (2 * x_value)
 
def main():
    """Main functions"""
    x_val = int(input())
    y_val = int(input())
    z_val = int(input())
 
    print(x_val + 1)
    print(str((7*y_val**3) + (2*y_val**2) - (31*y_val) + 1))
    print(str(-z_val))
    print(str((x_val + y_val) * (x_val - y_val)))
    print(str(call_function_five(x_val, y_val, z_val)))
 
 
main()