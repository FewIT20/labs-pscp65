"""IG: few.pz"""
from itertools import count


def main():
    """Main function"""
    x_val = []
    countable = int(input())
    pattern = input()
    for _ in range(countable-1):
        value = input()
        if pattern in value:
            x_val.append("Yes")
        else:
            x_val.append("No")
    print(*x_val, sep="\n")
main()
