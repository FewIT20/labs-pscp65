"""IG: few.pz"""
def main():
    """ Main function """
    line = input().split()
    value = 0
    keep_items = 0
    for i in line:
        changed_value = int(i)
        value = abs(changed_value - value)
        keep_items += value
        value = changed_value
    print(keep_items)
main()
