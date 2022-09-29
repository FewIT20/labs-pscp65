"""IG: few.pz"""
def main():
    """ Main function """
    text = input()
    LAYER_1, LAYER_2, LAYER_3 = '.', '.', '#'
    for value in text:
        LAYER_1 += '.#..'
        LAYER_2 += '#.#.'
        LAYER_3 += '.' + value + '.#'
    for value in range(2, len(text), 3):
        LAYER_1 = LAYER_1[:value*4+2] + '*' + LAYER_1[value*4+3:]
        LAYER_2 = LAYER_2[:value*4+1] + '*.*' + LAYER_2[value*4+4:]
        LAYER_3 = LAYER_3[:value*4] + '*.' + text[value] + '.*' + LAYER_3[value*4+5:]
    print(LAYER_1)
    print(LAYER_2)
    print(LAYER_3)
    print(LAYER_2)
    print(LAYER_1)
main()