"""IG: few.pz"""
def main():
    """Main function"""
    text = input()
    count = len(text)
    for i in range(0, count):
        print(" "*(count-(i+1)-1)+text[0:i:+1])
    for i in range(0, count):
        print(text[i+1:count:])
main()
