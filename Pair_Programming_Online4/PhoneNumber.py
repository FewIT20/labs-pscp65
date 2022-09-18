"""IG: few.pz"""
def main():
    """Main function"""
    phone_number = input()
    nation = input()
    if len(phone_number) == 9:
        if nation == "Domestic":
            print(phone_number[0] + " " + phone_number[1:5] + " " +phone_number[5:])
        else:
            print("+66"+" " + phone_number[1:5] + " " + phone_number[5:])
    else:
        if nation == "Domestic":
            print(phone_number[0:2:] + " " + phone_number[2:6] + " " + phone_number[6:])
        else:
            print("+66" + phone_number[1] + " " + phone_number[2:6] + " " + phone_number[6:])
main()
