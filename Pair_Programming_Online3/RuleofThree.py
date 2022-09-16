"""IG: few.pz"""
def insert_into_list(x_val, price, weight, is_clear=False):
    """Insert into list Function"""
    if is_clear:
        x_val.clear()
    x_val.append(price)
    x_val.append(weight)

def main():
    """Main function"""
    value = int(input())
    x_val = []
    counter = 0
    for _ in range(value):
        price = float(input())
        weight = float(input())
        if x_val == []:
            insert_into_list(x_val, price, weight)
            counter = weight/price
        if counter > weight/price and counter != 0:
            continue
        elif counter < weight/price and counter != 0:
            counter = weight/price
            insert_into_list(x_val, price, weight, True)
        elif counter == weight/price and counter != 0:
            if x_val[0] > price:
                insert_into_list(x_val, price, weight, True)
    print("%.2f %.2f"%(x_val[0], x_val[1]))
main()
