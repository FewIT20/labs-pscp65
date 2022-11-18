"""IG: few.pz"""
def main():
    """ Main function """
    price = float(input())
    lid_ex = int(input())
    lid_ex_milk = int(input())
    bottle_ex = int(input())
    bottle_ex_milk = int(input())
    money = float(input())

    buy = money // price
    total_milk = lid = bottle = buy
    while lid >= lid_ex or bottle >= bottle_ex:
        milk_from_lid = (lid // lid_ex) * lid_ex_milk
        milk_from_bottle = (bottle // bottle_ex) * bottle_ex_milk
        get_milk = milk_from_lid + milk_from_bottle
        lid = get_milk + lid % lid_ex
        bottle = get_milk + bottle % bottle_ex
        total_milk += get_milk
    print(int(total_milk))
main()
