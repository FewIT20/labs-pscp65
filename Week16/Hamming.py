"""IG: few.pz"""
def main():
    """ Main function """
    text = list(input())
    compare_text = list(input())
    count = 0
    for i in range(len(text)):
        if text[i] != compare_text[i]:
            count += 1
    print(count)
main()
