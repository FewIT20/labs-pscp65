"""IG: few.pz"""
def main():
    """ Main function """
    binary = input()
    string_builder = ""
    for bit in binary:
        if bit == "1":
            string_builder += "0"
        elif bit == "0":
            string_builder += "1"
    print(string_builder.lstrip("0"))
main()
