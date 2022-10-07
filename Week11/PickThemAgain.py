"""IG: few.pz"""
def main():
    """Main function"""
    x_val = []
    value = input().split(" ")
    can_find_value = False
    for i in range(len(value)):
        y_val = int(value[i])
        if y_val % 3 == 0 or y_val % 5 == 0:
            x_val.append(int(value[i]))
            can_find_value = True
    x_val.reverse()
    if can_find_value:
        print(*x_val, sep="\n")
    else:
        print("Nope")
main()
