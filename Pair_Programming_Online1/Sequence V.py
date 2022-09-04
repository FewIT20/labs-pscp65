"""IG: few.pz"""
import math
def main():
    """Main function"""
    x_val = int(input())
    y_val = math.ceil(x_val/7)
    for _ in range(y_val):
        for _ in range(7):
            if x_val < 1:
                break
            print(x_val, end=" ")
            x_val -= 1
        print()
main()
