"""IG: few.pz"""
def main():
    """Main function"""
    value = [float(input()), float(input()), float(input())]
    if value[0] > value[1]:
        value[1], value[0] = value[0], value[1]
    if value[1] > value[2]:
        value[1], value[2] = value[2], value[1]
    if value[0] > value[1]:
        value[1], value[0] = value[0], value[1]

    process = ((value[0]**2)+(value[1]**2))**0.5
    if value[2] <= process <= value[2]+0.01:
        print("Yes")
    else:
        print("No")
main()
