"""IG: few.pz"""
def main():
    """Main function"""
    value_a = int(input())
    value_b = int(input())
    value_gold = int(input())
    if value_gold % 5 > value_a or (value_a + (value_b * 5)) < value_gold:
        print(-1)
    else:
        if value_b * 5 >= value_gold:
            small = value_gold % 5
        else:
            small = value_gold-(value_b*5)
        print(small)
main()
