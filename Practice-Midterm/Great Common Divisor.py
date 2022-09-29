"""IG: few.pz"""
import math

def main():
    """Main function"""
    value = input().split()
    x_val = int(value[0])
    y_val = int(value[1])
    
    print(math.gcd(x_val, y_val))
main()
