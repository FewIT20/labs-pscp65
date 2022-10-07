"""IG: few.pz"""
def main():
    """Main function"""
    count = int(input())
    value = []
    for _ in range(1, count + 1):
        value.append(input())
    value = sorted(value, key=lambda x: (len(x), x))
    print(*value, sep="\n")
main()
