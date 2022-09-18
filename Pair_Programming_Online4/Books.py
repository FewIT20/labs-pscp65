"""IG: few.pz"""
import math

def main():
    """Main function"""
    value_1 = int(input())
    value_2 = int(input())
    value_3 = int(input())
    value_4 = int(input())
    count = 0
    day = 0
    counter = 0
    while True:
        value_5 = math.ceil((value_3 / value_4) * value_2)
        if count == value_1:
            break
        if value_5 >= value_2:
            break
        counter += value_5
        if counter >= value_2:
            counter = 0
            count += 1
        value_3 += 1
        value_4 += 1
        day += 1
    day += (value_1-count)
    print(day)
main()
