"""IG: few.pz"""
def scaled_maxtrix(value, count):
    """ Scaled maxtrix """
    return value[count] / max(value)
def main():
    """ Main function """
    lst = []
    value = []
    row = int(input())
    column = int(input())
    for _ in range(row * column):
        lst.append(float(input()))
    absolved = abs(min(lst))
    for i in range(row * column):
        value.append(lst[i] + absolved)
    count = 0
    for _ in range(row):
        for _ in range(column):
            print("%.2f" % scaled_maxtrix(value, count), end=" ")
            count += 1
        print()
main()
