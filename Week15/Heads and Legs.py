"""IG: few.pz"""
def main():
    """ Main function """
    head = int(input())
    leg = int(input())
    rabbit, ghost = divmod(leg-2 * head, 2)
    bird = head - rabbit
    if rabbit >= 0 and bird >= 0 and ghost == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
