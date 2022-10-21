"""IG: few.pz"""
def main():
    """ Main function """
    num = int(input())
    value = []
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            value.append(i)
    print(sum(value))
main()
