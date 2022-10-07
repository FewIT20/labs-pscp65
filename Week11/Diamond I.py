"""IG: few.pz"""
def main():
    """Main functions"""
    count_a = int(input())
    count_b = int(input())
    value = []
    attempted = []
    for _ in range(count_a):
        diamond = input().split()
        value.append(diamond)
    for i in range(count_b):
        calculate = 0
        for j in value:
            calculate += int(j[i])
        attempted.append(calculate)
    print(max(attempted))
main()
