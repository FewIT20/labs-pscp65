"""IG: few.pz"""
def main():
    """ Main function """
    _ = int(input())
    _ = int(input())
    bis_row = int(input())
    bis_col = int(input())
    other_row = int(input())
    other_col = int(input())
    enemy = int(input())
    target_row = int(input())
    target_col = int(input())

    if abs(target_row - bis_row) == abs(target_col - bis_col):
        if target_row - bis_row < 0:
            step_row = -1
        else:
            step_row = 1
        if target_col - bis_col < 0:
            step_col = -1
        else:
            step_col = 1

        if target_row == other_row and target_col == other_col and enemy == 1:
            print("Yes")
            return
        if target_row == other_row and target_col == other_col and enemy == 0:
            print("No")
            return
        direction = []

        temp_row = bis_row
        temp_col = bis_col
        while temp_row != target_row and temp_col != target_col:
            direction.append((temp_row, temp_col))
            temp_row += step_row
            temp_col += step_col
        if (other_row, other_col) in direction:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
main()
