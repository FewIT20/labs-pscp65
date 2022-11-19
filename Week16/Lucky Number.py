"""IG: few.pz"""


def main(number):
    """ Main function """
    number1 = range(-1, number+1, 2)
    i = 2
    while number1[i:]:
        number1 = sorted(set(number1) - set(number1[number1[i]::number1[i]]))
        i += 1
    print(*(number1[1:number+1]), sep=(' '))


main(int(input()))
