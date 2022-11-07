"""IG: few.pz"""
def main():
    """ Main function """
    answer = input()
    guess = input()
    point_b = 0
    point_w = 0
    point_b += sum([1 for i in range(4) if answer[i] == guess[i]])
    value = list(answer)
    for i in guess:
        if i in value:
            point_w += 1
            value.remove(i)
    point_w -= point_b
    word_b = "B" * point_b
    word_w = "W" * point_w
    word_zero = "O" * (4 - point_b - point_w)
    print(word_b + word_w + word_zero)
main()
