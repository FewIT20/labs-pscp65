"""IG: few.pz"""
def main():
    """Main function"""
    value = int(input())
    if  value > 1:
        for i in range(2, value):
            if value % i == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
main()
