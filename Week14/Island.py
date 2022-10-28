"""IG: few.pz"""
def flood_fill(i, j, row, col, island):
    """Return 1 if (i, j) and its neighbors are part of the island, 0 otherwise."""
    count = 0
    if island[i][j] == 1:
        island[i][j] = 2
        eight_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        new_positions = [(i+x, j+y) for x, y in eight_directions]
        for pos_x, pos_y in new_positions:
            if pos_x in range(0, row) and pos_y in range(0, col):
                flood_fill(pos_x, pos_y, row, col, island)
        count = 1
    return count

def count_island(row, col, island):
    """Return total number of islands in the map."""
    count = 0
    for i in range(row):
        for j in range(col):
            count = count + flood_fill(i, j, row, col, island)
    return count

def make_matrix():
    """Return number of rows, number of columns and matrix of island map."""
    row, col = [int(x) for x in input().split()]
    island = [[int(x) for x in input().split()] for _ in range(row)]
    return row, col, island

def main():
    """ Main function """
    row, col, island = make_matrix()
    print(count_island(row, col, island))
main()
