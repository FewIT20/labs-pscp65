"""IG: few.pz"""
def main():
    """Main function"""
    text = input()
    count = len(text)
    for i in range(0, count + 1):
        if i == 0:
            continue
        elif i != count:
            print(" ", end="")
        print(" "*(count-i-1)+text[0:i:+1])
    for i in range(0, count + 1):
        if text[i+1:count:] == "":
            continue
        print(""+text[i+1:count:]+"")
main()
