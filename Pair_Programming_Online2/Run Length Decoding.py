"""IG: few.pz"""
def main():
    """Main function"""
    x_val = str(input())
    y_val = ""
    for string in x_val:
        if string.isnumeric():
            y_val += string
        else:
            print(string * int(y_val), end="")
            y_val = ""
main()
