"""IG: few.pz"""
def main():
    """Main function"""
    x_val = []
    y_val = []
    amount = int(input())
    for _ in range(amount):
        card = input()
 
        if card in "jkqJKQ":
            card = 10
            x_val.append(card)
        elif card in "Aa":
            y_val.append("A")
        else:  # number
            x_val.append(int(card))
 
    while len(y_val) > 0:
 
        y_val.remove("A")
 
        if sum(x_val) + 11 > 21:
            x_val.append(1)
        elif sum(x_val) == 10 and len(y_val) == 1:
            x_val.append(1)
        else:
            x_val.append(11)
 
    print(sum(x_val))
 
main()
