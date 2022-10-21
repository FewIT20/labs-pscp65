"""IG: few.pz"""
def main():
    """ Main function """
    x_val = []
    value = input().replace(".", "")
    arr = value.split()
    for raw in arr:
        total = raw.count("a") + raw.count("e") + raw.count("i") + raw.count("o") + raw.count("u")
        if total >= 2:
            x_val.append(raw)
    if len(x_val) == 0:
        x_val.append("Nope")
    x_val.sort()
    for raw in x_val:
        print(raw)
main()
