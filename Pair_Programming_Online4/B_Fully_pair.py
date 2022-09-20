"""IG: few.pz"""
def main():
    """Main function"""
    value = input().lower()
    test = ''
    result = ''
    count = 0
    for idx in value:
        if test.count(idx) <= 0:
            test += idx
    for idx in test:
        if (int(value.count(idx)) % 2) == 1:
            count += 1
            result += idx
    print('fully paired' if count == 0 else result)
main()
