"""IG: few.pz"""
def main():
    """ Main function """
    kangaroo = [int(input()) for _ in range(3)]
    print(max(kangaroo[2] - kangaroo[1], kangaroo[1] - kangaroo[0]) - 1)
main()
