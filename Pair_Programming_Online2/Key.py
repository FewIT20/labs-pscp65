"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    first = 0
    for i in value:
        first += int(i)
    seconds = int(value[-3:])*10
    total = first + seconds
    if total < 1000:
        total += 1000
    print(str(total)[-4:])
main()
