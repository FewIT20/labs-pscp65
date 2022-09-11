"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    if value.isnumeric():
        print("Number")
    elif value.isupper():
        print("Uppercase")
    elif value.islower():
        print("Lowercase")
    elif value.istitle():
        print("Title")
    elif value.isspace():
        print("Space")
    else:
        print("Other")
main()
