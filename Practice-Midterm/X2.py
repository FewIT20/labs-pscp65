"""IG: few.pz"""
def main():
    """Main function"""
    value = input().split()
    x_one = int(value[0])
    average_of_s = int(value[1])
    print("%d"  % (average_of_s * 2 - x_one))
main()
