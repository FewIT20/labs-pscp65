"""IG: few.pz"""
def main():
    """ Main function """
    row = int(input())
    count = ""
    for _ in range(row):
        area = input().replace(" ", "")
        count += area
    print(len(count))
main()
