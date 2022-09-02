"""IG: few.pz"""
def main():
    """Main function"""
    my_pos_x = float(input())
    my_pos_y = float(input())
    radius = float(input())
    pos_x = float(input())
    pos_y = float(input())
    my_redius = float(input())

    distance = (((my_pos_x-pos_x)**2) +((my_pos_y-pos_y)**2))**0.5
    if distance >= radius + my_redius:
        print("No")
    elif distance < radius + my_redius:
        print("Yes")
main()
