"""IG: few.pz"""
def check_disk(name, disk):
    """main"""
    if disk == "128 GB":
        return 0
    elif disk == "256 GB":
        return 4000
    elif disk == "512 GB":
        return 12000
    elif disk == "1 TB":
        if name == "iPhone 13 mini" or name == "iPhone 13":
            return -1
        else:
            return 20000
    else:
        return -1

def main():
    """Main function"""
    idx1 = input()
    disk = input()
    disk = check_disk(idx1, disk)
    if disk == -1:
        print('Not Available')
    else:
        if idx1 == "iPhone 13 mini":
            print(25900 + disk)
        elif idx1 == "iPhone 13":
            print(29900 + disk)
        elif idx1 == "iPhone 13 Pro":
            print(38900 + disk)
        elif idx1 == "iPhone 13 Pro Max":
            print(42900 + disk)
        else:
            print('Not Available')
main()
