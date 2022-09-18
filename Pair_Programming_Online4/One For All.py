"""IG: few.pz"""
def main():
    """Main function"""
    counter = int(input())
    exp = 0
    value = ""
    for _ in range(counter):
        txt = input()
        exp += 1
        if exp == counter:
            value += (txt + "_%d" % counter)
        elif exp % 2 == 0:
            value += (txt + "-" * exp)
        else:
            value += (txt + "*" * exp)
    print(value)
main()
