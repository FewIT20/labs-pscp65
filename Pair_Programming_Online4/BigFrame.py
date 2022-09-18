"""IG: few.pz"""
def main():
    """Main function"""
    text_1 = input().rstrip()
    text_2 = input().rstrip()
    text_3 = input().rstrip()
    text_4 = input().rstrip()
    text_5 = input().rstrip()
    line = max(len(text_1), len(text_2), len(text_3), len(text_4), len(text_5))
    print("**" + "*" * line + "**")
    print("* " + text_1 + " " * (line - len(text_1)) + " *")
    print("* " + text_2 + " " * (line - len(text_2)) + " *")
    print("* " + text_3 + " " * (line - len(text_3)) + " *")
    print("* " + text_4 + " " * (line - len(text_4)) + " *")
    print("* " + text_5 + " " * (line - len(text_5)) + " *")
    print("**" + "*" * line + "**")
main()
