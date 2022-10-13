"""IG: few.pz"""
def main():
    """Main function"""
    set_n = set()
    set_m = set()
    num_n = int(input())
    num_m = int(input())
    for _ in range(num_n):
        set_n.add(int(input()))
    for _ in range(num_m):
        set_m.add(int(input()))
    value = set_n.difference(set_m)
    value = sorted(value)
    for i in value:
        print(i, end=" ")
main()
