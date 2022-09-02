"""IG: few.pz"""
def main():
    """Main function"""
    x_val = []
    checked = int(input())
    while True:
        value = int(input())
        if value == -1:
            break
        x_val.append(value)
        if sum(x_val) == checked:
            break
    print(sum(x_val))
main()
