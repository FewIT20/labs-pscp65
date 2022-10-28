"""IG: few.pz"""
def main():
    """ Main function """
    lst = []
    row = int(input())
    column = int(input())
    for _ in range(row * column):
        lst.append(int(input()))
    for i in range(row):
        for j in range(column):
            print(lst[i * column + j], end=" ")
        print()
main()
