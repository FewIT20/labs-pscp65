"""IG: few.pz"""
import math

def calculate_length(value, length):
    """Calculate length"""
    return length-len(value)

def main():
    """Main function"""
    length = int(input())
    side = input()
    value = input()
    if side == "left":
        print(value + " "*calculate_length(value, length))
    elif side == "center":
        left_side = math.ceil(calculate_length(value, length)/2)
        right_side = math.floor(calculate_length(value, length)/2)
        print(" "*left_side + value + " "*right_side)
    elif side == "right":
        print(" "*calculate_length(value, length) + value)
main()
