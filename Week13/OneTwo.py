"""IG: few.pz"""
def one_two(value):
    """OneTwo Function"""
    if value == 1:
        return "1"
    elif value == 2:
        return "2"
    else:
        return one_two(value - 1) + one_two(value - 2)

def main():
    """ Main function """
    print(one_two(int(input())))
main()
