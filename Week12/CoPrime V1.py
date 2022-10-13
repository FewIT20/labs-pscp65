"""IG: few.pz"""
def main():
    """Main function"""
    value_1 = int(input())
    value_2 = int(input())
    check = 1
    for i in range(1, value_1 + 1):
        if value_1 % i == 0 and value_2 % i == 0:
            check = i
    if check == 1:
        print("YES")
        print(check)
    else:
        print("NO")
        print(check)
main()
