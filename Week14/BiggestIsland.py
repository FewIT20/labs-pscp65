"""IG: few.pz"""
def flood_fill(i, j, row, col, island):
    """Return 1 if (i, j) and its neighors are part of the island, 0 otherwise."""
    count = 0
    if island[i][j] == 1:
        count += 1
        island[i][j] = 2
        eight_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        new_positions = [(i+x, j+y) for x, y in eight_directions]
        for pos_x, pos_y in new_positions:
            if pos_x in range(0, row) and pos_y in range(0, col):
                count += flood_fill(pos_x, pos_y, row, col, island)
    return count

def count_island(row, col, island):
    """Return total number of islands in the map."""
    area = []
    for i in range(row):
        for j in range(col):
            area.append(flood_fill(i, j, row, col, island))
    return area

def main():
    """ Main function """
    row, col = [int(x) for x in input().split()]
    island = [[int(x) for x in input().split()] for _ in range(row)]
    print(max(count_island(row, col, island)))
main()
