"""IG: few.pz"""
def main():
    """Main function"""
    original_cost = int(input())
    promotion_caps_of_coke = int(input())
    special_cost = int(input())
    amount = int(input())

    price, caps_of_coke = original_cost, 0
    currently_balance = 0
    while amount > 0:
        caps_of_coke += 1
        currently_balance += price
        price = original_cost #Back to original price
        if promotion_caps_of_coke == 0:
            currently_balance = original_cost * amount
            break
        if caps_of_coke == promotion_caps_of_coke:
            price = special_cost
            caps_of_coke = 0
        amount -= 1
    print(currently_balance)
main()
