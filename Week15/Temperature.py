"""IG: few.pz"""
def main():
    """ Main function """
    temp = float(input())
    convert_from = input()
    convert_to = input()

    if convert_from == 'K':
        temp = temp - 273.15
    elif convert_from == 'F':
        temp = (temp - 32) * (5/9)
    elif convert_from == 'R':
        temp = (temp - 491.67) * (5/9)
    elif convert_from == 'C':
        temp = temp

    if convert_to == 'K':
        temp = temp + 273.15
    elif convert_to == 'F':
        temp = (temp * (9/5)) + 32
    elif convert_to == 'R':
        temp = (temp * (9/5)) + 491.67
    elif convert_to == 'C':
        temp = temp
    print("%.2f" % temp)
main()
