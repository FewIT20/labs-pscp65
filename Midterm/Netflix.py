"""IG: few.pz"""
def display_package(premium, standard, basic, mobile, total):
    """Display package functions"""
    if premium > 0:
        print("Premium x %d" % premium)
    if standard > 0:
        print("Standard x %d"% standard*(standard > 0))
    if basic > 0:
        print("Basic x %d" % basic*(basic > 0))
    if mobile > 0:
        print("Mobile x %d" % mobile*(mobile > 0))
    print("Total = %d THB" % total)

def main():
    """Main function"""
    number_of_screen = int(input())
    number_of_phone = int(input())
    input()
    input()
    watch_tv = input().lower()
    hdo = input().lower()
    ultra = input().lower()

    counter_premium = 0
    counter_standard = 0
    counter_basic = 0
    counter_mobile = 0
    total = 0
    while number_of_screen > 0 or number_of_phone > 0:
        if (ultra == "yes" or hdo == "yes" or watch_tv == "yes") \
            and (number_of_screen >= 3 or number_of_phone >= 3):
            total += 419
            counter_premium += 1
            number_of_screen -= 4
            number_of_phone -= 4
        elif (hdo == "yes" or watch_tv == "yes") \
            and (number_of_screen >= 2 or number_of_phone >= 2):
            total += 349
            counter_standard += 1
            number_of_screen -= 2
            number_of_phone -= 2
        elif watch_tv == "yes" and ultra == "no" and hdo == "no":
            total += 279
            counter_basic += 1
            number_of_screen -= 1
            number_of_phone -= 1
        else:
            if ultra == "yes":
                total += 419
                counter_premium += 1
                number_of_screen -= 4
                number_of_phone -= 4
            elif hdo == "yes":
                total += 349
                counter_standard += 1
                number_of_screen -= 2
                number_of_phone -= 2
            elif watch_tv == "yes":
                total += 279
                counter_basic += 1
                number_of_screen -= 1
                number_of_phone -= 1
            else:
                total += 99
                counter_mobile += 1
                number_of_screen -= 1
                number_of_phone -= 1
    display_package(counter_premium, counter_standard, counter_basic, counter_mobile, total)
main()
