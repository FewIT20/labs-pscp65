"""IG: few.pz"""
import math

def calucate_length(value, length):
    """Calculate length"""
    return length-len(value)

def main():
    """Main function"""
    length = int(input())
    side = input()
    value = input()
    if side == "left":
        print(value + " "*calucate_length(value, length))
    elif side == "center":
        left_side = math.ceil(calucate_length(value, length)/2)
        right_side = math.floor(calucate_length(value, length)/2)
        print(" "*left_side + value + " "*right_side)
    elif side == "right":
        print(" "*calucate_length(value, length) + value)
main()
