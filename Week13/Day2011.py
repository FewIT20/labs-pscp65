"""IG: few.pz"""
def main():
    """ Main function """
    date = int(input())
    month = int(input())
    number = 0
    data = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(month):
        number += data[i]
    value = (number + date) % 7
    if value == 1:
        print("Saturday")
    elif value == 2:
        print("Sunday")
    elif value == 3:
        print("Monday")
    elif value == 4:
        print("Tuesday")
    elif value == 5:
        print("Wednesday")
    elif value == 6:
        print("Thursday")
    else:
        print("Friday")
main()
