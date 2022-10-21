"""IG: few.pz"""
def decimal_to_base_two(decimal):
    """ Decimal to BaseTwo """
    base_two = []
    while decimal > 0:
        base_two.append(decimal % 2)
        decimal //= 2
    base_two.reverse()
    return base_two

def main():
    """ Main function """
    num = int(input())
    if num == 0:
        print(0)
    for raw in decimal_to_base_two(num):
        print(raw, end='')
main()
