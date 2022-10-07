"""IG: few.pz"""
import json

def main():
    """Main function"""
    value = []
    x_val = json.loads(input())
    can_find_value = False
    for i in range(len(x_val)):
        y_val = int(x_val[i])
        if y_val % 2 == 0:
            value.append(int(x_val[i]))
            can_find_value = True
    if can_find_value:
        print(*value, sep="\n")
    else:
        print("Nope")
main()
