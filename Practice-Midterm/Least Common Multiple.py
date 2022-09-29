"""IG: few.pz"""
import math

def main():
    """Main function"""
    x_value = int(input())
    y_value = int(input())
    lcm = (x_value * y_value) / math.gcd(x_value, y_value)
    print("%d" % (lcm))
main()
