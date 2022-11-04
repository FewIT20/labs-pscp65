"""IG: few.pz"""
def main():
    """ Main function """
    total = int(input())
    valid = [int(valid) for valid in input().split()]
    value = 0
    valid.sort()
    while valid[0] != 0:
        for i in range(1, total):
            valid[i] = valid[i] - 1
        value += 1
        valid.sort()
    print(value)
main()
