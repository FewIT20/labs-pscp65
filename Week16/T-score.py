"""IG: few.pz"""


def main():
    """ Main function """
    amount = int(input())
    int(input())
    value = 0
    value_with_power_2 = 0
    list_score = []
    for _ in range(amount):
        score_student = int(input())
        value += score_student
        value_with_power_2 += (score_student**2)
        list_score.append(score_student)
    standard_deviation = (
        ((amount*(value_with_power_2))-(value**2))/(amount*(amount-1)))**0.5
    sum_x = value/amount
    for i in list_score:
        sum_z = (int(i)-sum_x) / standard_deviation
        print('%.2f' % (50 + 10*(sum_z)))


main()
