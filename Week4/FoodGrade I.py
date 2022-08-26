"""IG: few.pz"""
def find_wing_chicken():
    """Find the wing chicken"""
    wing = int(input())
    if 50 <= wing <= 70:
        return wing
    else:
        return 0

def main():
    """Main function"""
    x_val = list()
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())
    x_val.append(find_wing_chicken())

    value = len(x_val) - x_val.count(0)
    print(value)
main()
