"""IG: few.pz"""
def main():
    """Main function"""
    text = input()
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    for i in text:
        if i == "U":
            line1 += "  *   "
            line2 += " ***  "
            line3 += "* * * "
            line4 += "  *   "
            line5 += "  *   "
        elif i == "D":
            line1 += "  *   "
            line2 += "  *   "
            line3 += "* * * "
            line4 += " ***  "
            line5 += "  *   "
        elif i == "L":
            line1 += "  *   "
            line2 += " *    "
            line3 += "***** "
            line4 += " *    "
            line5 += "  *   "
        elif i == "R":
            line1 += "  *   "
            line2 += "   *  "
            line3 += "***** "
            line4 += "   *  "
            line5 += "  *   "
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

main()
