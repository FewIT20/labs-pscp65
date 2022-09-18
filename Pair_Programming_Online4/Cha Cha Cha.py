"""IG: few.pz"""
import math

def main():
    """Main function"""
    x_val = int(input())
    total = 0
    for _ in range(x_val):
        test = int(math.ceil(float(input())))
        total += test * 8720
    print(total)
main()
