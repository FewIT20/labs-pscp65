"""IG: few.pz"""
def dodamaze(maze, start, stop, path="", keep=None):
    """maze"""
    if keep == None:
        keep = []
    i, j = start
    if maze[i][j] == "Y":
        keep.append(path)
    checking = [(i-1, j, "E"), (i, j+1, "F"), (i+1, j, "G"), (i, j-1, "H")]
    checking = filter(lambda a: a[0] in range(10) and a[1] in range(20), checking)
    for k in filter(lambda a: maze[a[0]][a[1]] in " Y", checking):
        new = maze.copy()
        new[i] = new[i][:j] + "P" + new[i][j+1:]
        dodamaze(new, k[:2], stop, path + k[2], keep)
    return keep
def main():
    """Maze"""
    maze = [input() for _ in range(10)]
    [start] = [(i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == "X"]
    stop = [(i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == "Y"]
    paths = []
    for i in stop:
        paths += sorted(dodamaze(maze, start, i))
    path = min(paths, key=len)
    for i, j in ("EU", "FR", "GD", "HL"):
        path = path.replace(i, j)
    print(path)
    print(len(path))
    print("You will make it on time!" if len(path)*23 < 10*60 else "You won't make it on time.")
main()
