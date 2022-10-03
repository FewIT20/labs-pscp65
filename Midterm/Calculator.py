"""IG: few.pz"""
def main():
    """Main function"""
    string_builder = ""
    value = int(input())
    for i in range(value):
        if value > 1:
            string_builder += str(i + 1)
            if i == value - 1:
                string_builder += "="
            else:
                string_builder += "+"
        else:
            string_builder += "1"
            break
    print(len(string_builder))
main()
