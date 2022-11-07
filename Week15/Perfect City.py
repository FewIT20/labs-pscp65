"""IG: few.pz"""
import math

def get_list(point_x):
    """ Get list function """
    value_1, value_2 = point_x
    if isinstance(value_1, float):
        return [(math.floor(value_1), value_2), (math.ceil(value_1), value_2)]
    else:
        return [(value_1, math.floor(value_2)), (value_1, math.ceil(value_2))]

def distance(point_x, point_y):
    """ Distance function """
    value_1, value_2 = point_x
    value_3, value_4 = point_y
    value = abs(value_1 - value_3) + abs(value_2 - value_4)
    return value

def main():
    """ Main function """
    point_x = float(input()), float(input())
    point_y = float(input()), float(input())
    calculate = min(distance(point_x, i) + distance(i, j) + distance(j, point_y) \
        for i in get_list(point_x) for j in get_list(point_y))
    print('%.2f' % calculate)
main()
