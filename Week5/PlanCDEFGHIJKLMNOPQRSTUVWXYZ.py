"""IG: few.pz"""
def main():
    """Main function"""
    order = input()

    value = [float(input()), float(input()), float(input())]
    if value[0] > value[1]:
        value[1], value[0] = value[0], value[1]
    if value[1] > value[2]:
        value[1], value[2] = value[2], value[1]
    if value[0] > value[1]:
        value[1], value[0] = value[0], value[1]

    if order.lower() == "ascend":
        print("%.2f, %.2f, %.2f " %(value[0], value[1], value[2]))
    elif order.lower() == "descend":
        print("%.2f, %.2f, %.2f " %(value[2], value[1], value[0]))

main()
