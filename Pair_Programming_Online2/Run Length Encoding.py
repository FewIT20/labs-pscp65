"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    checker = value[0]
    count = 0
    x_val = ""
    for i in range(0, len(value)):
        if checker == value[i]:
            count += 1
        else:
            x_val += str(count) + value[i-1]
            checker = value[i]
            count = 1
    x_val += str(count) + value[-1]
    print(x_val)

main()
