"""IG: few.pz"""
def main():
    """Main function"""
    cost = float(input())
    years = int(input())
    percent = 381
    cost = int(cost * 100)
    for _ in range(years):
        interest = cost * percent
        cost = cost + interest // 10000
    value_1 = str(cost)
    value_2 = value_1[-2::]
    value_3 = value_1[::-1]
    value_3 = value_3[2::]
    value_3 = value_3[::-1]
    if value_3 == "":
        value_3 = "0"
    if value_2 == "":
        value_2 = "0"

    print("%d.%02d" % (int(value_3), int(value_2)))
main()
