"""IG: few.pz"""
def main():
    """Main function"""
    value_x = int(input())
    value_y = int(input())
    height = int((value_y-1)/2)
    final_height = height
    for _ in range(0, height+1):
        print((" ")*height+("*")*value_x)
        height -= 1
    for _ in range(0, final_height+1):
        height += 1
        if height >= 1:
            print((" ")*height+("*")*value_x)
main()
