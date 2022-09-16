"""IG: few.pz"""
def main():
    """Main function"""
    first_prize = input()
    last_two_digit_prize = input()
    front_three_digit_first_prize = input()
    front_three_digit_second_prize = input()
    last_three_digit_first_prize = input()
    last_three_digit_second_prize = input()
    lotto = input()
    balance = 0

    #First Prize!
    if lotto == first_prize:
        balance += 6000000

    #You so lucky! Last two digit is the same!
    if lotto[-2] == last_two_digit_prize[0] and \
        lotto[-1] == last_two_digit_prize[1]:
        balance += 2000

    #You so lucky! Front three digit is the same!
    if lotto[0] == front_three_digit_first_prize[0] \
        and lotto[1] == front_three_digit_first_prize[1]\
             and lotto[2] == front_three_digit_first_prize[2]:
        balance += 4000
    if lotto[0] == front_three_digit_second_prize[0] \
        and lotto[1] == front_three_digit_second_prize[1]\
             and lotto[2] == front_three_digit_second_prize[2]:
        balance += 4000

    #You so lucky! Last three digit is the same!
    if lotto[-1] == last_three_digit_first_prize[2] and \
        lotto[-2] == last_three_digit_first_prize[1] and \
            lotto[-3] == last_three_digit_first_prize[0]:
        balance += 4000
    if lotto[-1] == last_three_digit_second_prize[2] and \
        lotto[-2] == last_three_digit_second_prize[1] and \
            lotto[-3] == last_three_digit_second_prize[0]:
        balance += 4000

    #Similar prize
    if int(first_prize) == 0 and (int(lotto) == 999999 or int(lotto) == 1):
        balance += 100000
    elif int(first_prize) == 999999 and (int(lotto) == 0 or int(lotto) == 999998):
        balance += 100000
    elif (int(lotto)) == int(first_prize)+1 or (int(lotto)) == int(first_prize)-1:
        balance += 100000

    print(balance)
main()
