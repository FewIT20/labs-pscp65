"""IG: few.pz"""
def main():
    """Main function"""
    requirement1, requirement2 = int(input()), int(input())
    requirement3, requirement4 = int(input()), int(input())
    count1, count2 = int(input()), int(input())
    count3, count4 = int(input()), int(input())

    idx1 = requirement1 / count1
    idx2 = requirement2 / count2
    idx3 = requirement3 / count4
    idx4 = requirement4 / count3

    for _ in range(4):
        if idx1 <= idx2:
            idx1, idx2 = idx2, idx1
        if idx2 <= idx3:
            idx2, idx3 = idx3, idx2
        if idx3 <= idx4:
            idx3, idx4 = idx4, idx3
    print(int(idx1 + 0.999999999))
main()
