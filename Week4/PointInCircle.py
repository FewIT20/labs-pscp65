"""IG: few.pz"""
def main():
    """Main function"""
    x_val = float(input())
    y_val = float(input())
    radius = float(input())
    circle_x = float(input())
    circle_y = float(input())

    if ((x_val - circle_x)**2) + ((y_val - circle_y)**2) <= radius**2:
        print("True")
    else:
        print("False")
main()
