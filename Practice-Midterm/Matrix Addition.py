"""IG: few.pz"""
def create_matrix(row):
    """Create matrix"""
    matrix = []
    for _ in range(row):
        matrix.append([int(i) for i in input().split()])
    return matrix

def main():
    """Main function"""
    value = input()
    column = int(value.split()[0])
    row = int(value.split()[1])
    matrix1 = create_matrix(column)
    matrix2 = create_matrix(column)
    total = [0] * column
    for i in range(column):
        total[i] = [0] * row
    for i in range(column):
        for j in range(row):
            total[i][j] += matrix1[i][j] + matrix2[i][j]
    for i in range(column):
        for j in range(row):
            print(total[i][j], end=" ")
        print()
main()
