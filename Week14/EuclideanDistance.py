"""IG: few.pz"""
def distance(point_1, point_2):
    """ Calculate the distance between two points """
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5

def main():
    """ Main function """
    lst = []
    total = 0
    count = int(input())
    for _ in range(count):
        raw = input().split(" ")
        pos_x = int(raw[0])
        pos_y = int(raw[1])
        lst.append([pos_x, pos_y])
    for i in range(count - 1):
        total += distance(lst[i], lst[i + 1])
    print("%.2f" % total)
main()
