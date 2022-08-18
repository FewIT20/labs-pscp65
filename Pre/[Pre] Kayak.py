"""IG: few.pz"""

def main():
    """Main function"""
    length = int(input())
    lst = sorted([float(i)for i in input().split()])
    attemped = []
    while len(lst) > 2:
        if lst[1]-lst[0] > lst[2]-lst[1]:
            attemped.append(lst[2]-lst[1])
            for _ in range(2):
                lst.pop(1)
        else:
            attemped.append(lst[1]-lst[0])
            for _ in range(2):
                lst.pop(0)
    attemped.append(lst[1]-lst[0])
    print(int(sum(sorted(attemped)[:length - 1])))

main()
