"""IG: few.pz"""
def main():
    """Main function"""
    text1 = input()
    text2 = input()
    for i in range(0, max(len(text1), len(text2)) + 1):
        print(text2[:i] + text1[i:])
main()
