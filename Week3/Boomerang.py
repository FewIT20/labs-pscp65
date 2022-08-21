"""IG: fewpz"""

def main():
    """Main functions"""
    x_val = int(input())
    y_val = int(input())
    z_val = int(input())
 
    print(x_val + 1)
    print(str((7*y_val**3) + (2*y_val**2) - (31*y_val) + 1))
    print(str(-z_val))
    print(str((x_val + y_val) * (x_val - y_val)))
    print(str((y_val - ((y_val**2) - (4*x_val*z_val))**0.5) / (2 * x_val)))
 
 
main()
