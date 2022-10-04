"""IG: few.pz"""
def main():
    """Main function"""
    n_value = int(input())
    value = input()
    increment = 0
    while increment != n_value:
        x_value = "%02d" % (int(value[-2:]) + 1)
        hours = value[0:2].replace(":", "")
        if int(x_value) % 60 == 0 and int(x_value) != 0:
            x_value = "00"
            y_value = int(hours) + 1
            hours = str(y_value)
        if int(hours) % 24 == 0:
            hours = "0"
        value = hours + ":" + x_value
        if value.replace(":", "") == value.replace(":", "")[::-1]:
            increment = increment + 1
            print(value)
main()
