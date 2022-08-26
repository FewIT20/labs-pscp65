"""IG: few.pz"""
 
 
def main():
    """Main function"""
    x_val = int(input())
    y_val = int(input())
    if x_val > 0 and y_val > 0:
        print("Q1")
    elif x_val > 0 and y_val < 0:
        print("Q4")
    elif x_val < 0 and y_val > 0:
        print("Q2")
    elif x_val < 0 and y_val < 0:
        print("Q3")
    elif y_val == 0 and x_val != 0:
        print("X")
    elif x_val == 0 and y_val != 0:
        print("Y")
    elif x_val == 0 and y_val == 0:
        print("O")
 
 
main()
