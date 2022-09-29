"""IG: few.pz"""
def main():
    """Main function"""
    x_val, y_val = [int(x) for x in input().split()]
    total_xval = int(x_val)
    value = []
    counter = 0
    for i in range(2, total_xval + 1):
        value.append(i)
    while (len(value) != 0):
        point = value[0]
        y_list = []
        for i in range(0, len(value)):
            if value[i] % point == 0:
                y_list.append(value[i])
        for i in range(0, len(y_list)):
            value.remove(y_list[i])
            counter += 1
            if counter == y_val:
                print(y_list[i])
                break
main()
