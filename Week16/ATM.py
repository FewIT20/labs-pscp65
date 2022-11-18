"""IG: few.pz"""
def process_transaction(transaction, current_currency):
    """ Process Transaction """
    enum = transaction.split()
    if enum[0] == "D":
        current_currency += int(enum[1])
    elif enum[0] == "W":
        if current_currency >= int(enum[1]):
            current_currency -= int(enum[1])
        else:
            current_currency -= current_currency
    return current_currency

def main():
    """ Main function """
    currency = 0
    currency = int(input())
    while True:
        transaction = input()
        if transaction == "END":
            break
        currency = process_transaction(transaction, currency)
    print(currency)

main()
