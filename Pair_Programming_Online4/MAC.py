"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    if not (len(value) == 17 or len(value) == 14):
        return print("ERROR")

    character = "ABCDEFabcdef1234567890.:-"

    for i in value:
        if i not in character:
            return print("ERROR")
    if not (value.count("-") == 5 or value.count(":") == 5 or value.count(".") == 2):
        return print("ERROR")
    if value[2] == "-" and value[5] == "-" and value[8] == "-"\
         and value[11] == "-" and value[14] == "-":
        print("VALID 1")
    elif value[2] == ":" and value[5] == ":" and  value[8] == ":"\
         and value[11] == ":" and value[14] == ":":
        print("VALID 2")
    elif value[4] == "." and value[9] == "." and value[:4].isalnum()\
         and value[5:9].isalnum() and value[10:\
].isalnum():
        print("VALID 3")
    else:
        print("ERROR")
main()
