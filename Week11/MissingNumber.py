"""IG: few.pz"""
def main():
    """Main function"""
    x_val = []
    checked = []
    value = int(input())
    for i in range(value+1):
        checked.append(i)
    for _ in range(value):
        value1 = int(input())
        x_val.append(value1)
        if value1 == 0:
            break
    x_val.sort()
    for i in x_val:
        checked.remove(i)
    for i in checked:
        print(i)
main()
