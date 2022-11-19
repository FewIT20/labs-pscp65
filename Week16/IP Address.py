"""IG: few.pz"""
def main():
    """ Main function """
    text = input().split('.')
    if len(text) != 4:
        print('Invalid IPv4 address')
        return
    for i in text:
        for j in i:
            if not j.isnumeric():
                print('Invalid IPv4 address')
                return
        if int(i) > 255 or int(i) < 0:
            print('Invalid IPv4 address')
            return
    print(*[int(i) for i in text], sep='.')
main()

