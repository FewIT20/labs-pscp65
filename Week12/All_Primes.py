"""IG: few.pz"""
def main():
    """Main function"""
    value_1 = int(input())
    increment = 0
    for i in range(1, value_1 + 1):
        if  i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                increment += 1
    print(increment)
main()
