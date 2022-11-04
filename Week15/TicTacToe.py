"""IG: few.pz"""
def main():
    """ Main function """
    axis = []
    for _ in range(3):
        axis.append([i for i in input()])
    if (axis[0][0] == axis[1][1] == axis[2][2] and \
        axis[0][0] != '-' and axis[1][1] != '-' and axis[2][2] != '-')\
         or (axis[0][2] == axis[1][1] == axis[2][0] and axis[0][2] != '-' \
             and axis[1][1] != '-' and axis[2][0] != '-'):
        print(axis[1][1], "WIN")
    else:
        for j in range(3):
            if axis[0][j] == axis[1][j] == axis[2][j] and\
                 (axis[0][j] != '-' and axis[1][j] != '-' and axis[2][j] != '-'):
                print(axis[0][j], "WIN")
                break
            elif axis[j][0] == axis[j][1] == axis[j][2] and\
                 (axis[j][0] != '-' and axis[j][1] != '-' and axis[j][2] != '-'):
                print(axis[j][0], "WIN")
                break
        else:
            print("DRAW")
main()
