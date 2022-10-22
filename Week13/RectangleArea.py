"""IG: few.pz"""
def main():
    """ Main function """
    rec1x2, rec1y2, width1, height1 = [int(x) for x in input().split()]
    rec1x1 = rec1x2 + width1
    rec1y1 = rec1y2 + height1
    rec2x2, rec2y2, width2, height2 = [int(x) for x in input().split()]
    rec2x1 = rec2x2 + width2
    rec2y1 = rec2y2 + height2

    width = max(0, min(rec1x1, rec2x1) - max(rec1x2, rec2x2))
    height = max(0, min(rec1y1, rec2y1) - max(rec1y2, rec2y2))

    result = width * height

    if result > 0:
        print(width * height)
    else:
        print("no overlapping")
main()
