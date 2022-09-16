"""IG: few.pz"""
def main():
    """Main function"""
    order_food = float(input())
    promotion = float(input())
    discount = float(input())
    x_val = float(input())
    total = order_food + x_val
    if total >= promotion:
        total -= total*(discount/100)
    if order_food >= promotion:
        order_food -= order_food*(discount/100)
    if total > order_food:
        print("No %.03f" %(total - order_food))
    elif total < order_food:
        print("Yes %.03f" %(order_food - total))
    else:
        print("Yes")
main()
