"""IG: few.pz"""
def main():
    """Main function"""
    mypos_x = float(input())
    mypos_y = float(input())
    radius = float(input())
    pos_x = float(input())
    pos_y = float(input())

    distance = (((mypos_x-pos_x)**2) +((mypos_y-pos_y)**2))**0.5
    if distance <= radius:
        print("Yes")
    elif distance > radius:
        print("No")
main()
