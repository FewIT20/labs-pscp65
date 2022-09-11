"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    result = 1
    for string in value:
        if string == "A":
            if result == 2:
                result = 1
            elif result == 1:
                result = 2
        elif string == "B":
            if result == 3:
                result = 2
            elif result == 2:
                result = 3
        elif string == "C":
            if result == 1:
                result = 3
            elif result == 3:
                result = 1
    print(result)
main()
