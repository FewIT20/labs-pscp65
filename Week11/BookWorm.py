"""IG: few.pz"""
def main():
    """Main functions"""
    countable = int(input())
    for _ in range(countable):
        minute = float(input())
        value = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(value)):
            if sum(value[:i+1]) > minute:
                break
            i += 1
        print(i)
main()
