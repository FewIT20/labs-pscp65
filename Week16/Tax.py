"""IG: few.pz"""
def main():
    """ Main function """
    yearly = int(input())
    ccc = int(input())
    value_2 = 0
    value_1 = 0
    if ccc <= 600:
        value_2 += ((ccc) * 0.5)
    elif ccc <= 1800:
        value_2 += ((ccc - 600) * 1.50) + 300
    elif ccc > 1800:
        value_2 += ((ccc - 1800) * 4) + 2100
    if yearly == 6:
        value_1 = value_2 * 0.9
    elif yearly == 7:
        value_1 = value_2 * 0.8
    elif yearly == 8:
        value_1 = value_2 * 0.7
    elif yearly == 9:
        value_1 = value_2 * 0.6
    elif yearly >= 10:
        value_1 = value_2 * 0.5
    if yearly <= 5:
        print("%.2f " % value_2)
    elif yearly >= 6:
        print("%.2f"  % value_1)
main()
