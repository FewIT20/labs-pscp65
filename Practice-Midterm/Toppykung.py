"""IG: few.pz"""
def main():
    """Main function"""
    num = int(input())
    value = []
    for _ in range(num):
        text = input()
        if text not in value:
            value.append(text)
    value.sort()
    for i in value:
        print(i)
main()
