"""IG: few.pz"""
def main():
    """Main function"""
    original_cost = int(input())
    promotion_cap_of_coke = int(input())
    special_cost = int(input())
    amount = int(input())

    if promotion_cap_of_coke == 0:
        print(original_cost*amount)
        quit()
    if amount == 0:
        print(0)
        quit()

    howmany = (amount - 1)
    loop_count = howmany // promotion_cap_of_coke
    howmany_left = howmany % promotion_cap_of_coke
    price2loop = (original_cost*(promotion_cap_of_coke-1)) + special_cost

    total = original_cost + (loop_count * price2loop) + (howmany_left * original_cost)
    print(total)
main()
