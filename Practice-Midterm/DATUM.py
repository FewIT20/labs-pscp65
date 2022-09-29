"""IG: few.pz"""
def main():
    """Main function"""
    value = input().split()
    day = int(value[0])
    month = int(value[1])
    
    days = 0
    for i in range(1, month):
        if i == 4 or i == 6 or i == 9 or i == 11:
            days += 30
        elif i == 2:
            days += 28
        else:
            days += 31
    days += day
    if days % 7 == 1:
        print("Thursday")
    elif days % 7 == 2:
        print("Friday")
    elif days % 7 == 3:
        print("Saturday")
    elif days % 7 == 4:
        print("Sunday")
    elif days % 7 == 5:
        print("Monday")
    elif days % 7 == 6:
        print("Tuesday")
    elif days % 7 == 0:
        print("Wednesday")
main()
