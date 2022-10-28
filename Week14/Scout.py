"""IG: few.pz"""
def main():
    """ Main function """
    for _ in range(int(input())):
        lis1, lis2 = list(map(int, input().split())), sorted(list(map(int, input().split())))
        weight, egg = 0, 0
        for _ in range(lis1[0]):
            if weight + lis2[0] <= lis1[2] and egg < lis1[1]:
                weight += lis2[0]
                egg += 1
                lis2.pop(0)
            else:
                break
        print(egg)
main()
