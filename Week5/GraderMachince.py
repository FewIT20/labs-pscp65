"""IG: few.pz"""
def main():
    """Main function"""
    starter = int(input())
    breaker = int(input())
    total = 0
    print("pass :", end=" ")
    if starter < breaker:
        while starter <= breaker:
            if starter % 2 == 0:
                total += starter
                print("%d" % starter, end=" ")
            starter += 1
    else:
        while starter >= breaker:
            if starter % 2 == 0:
                total += starter
                print("%d" % starter, end=" ")
            starter -= 1
    print()
    print("Sum : %d" % total)
main()
