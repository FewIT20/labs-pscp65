"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    total = 0
    for character in value:
        if character == "o":
            total += 1
    print(total)
main()
