"""IG: few.pz"""
def main():
    """Main function"""
    count = int(input())
    for _ in range(count):
        word = input()
        word = word.replace('baka', '-').replace("bakka", "").\
            replace("ta", "").replace("ba", "").replace("ka", "")
        if word == "":
            print("yes")
        else:
            print("no")
main()
