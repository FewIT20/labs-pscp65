"""IG: few.pz"""
def main():
    """Main function"""
    cat_is_bug = True
    checker = 0
    countable_integer = 0

    highest = int(input())
    floor = int(input())
    for _ in range(1, floor + 1):
        jumping = int(input())
        checker = checker + jumping
        if jumping > highest:
            cat_is_bug = False
        elif checker == highest:
            countable_integer = countable_integer + 1
            checker = 0
        elif checker > highest:
            countable_integer = countable_integer + 1
            checker = jumping
    if checker > 0:
        countable_integer = countable_integer + 1
    if cat_is_bug:
        print("%d" % countable_integer)
    else:
        print("NO")

main()
