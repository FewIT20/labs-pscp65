"""IG: few.pz"""
def main():
    """Main function"""
    binary = input()
    even_or_odd = input().lower()
    string_builder = ""
    point_increment = 0
    for text in binary:
        if text == "1":
            point_increment += 1
        string_builder += text
    if even_or_odd == "even":
        if point_increment % 2 == 0:
            string_builder += str(0)
        else:
            string_builder += str(1)
    if even_or_odd == "odd":
        if point_increment % 2 == 0:
            string_builder += str(1)
        else:
            string_builder += str(0)
    print(string_builder)
main()
