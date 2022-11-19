"""IG: few.pz"""


def calculate_of_line(operator, line):
    """ Calculate of line """
    value = []
    if operator == "==":
        value.append(line)
    elif operator == "!=":
        value = [int(i) for i in range(0, 10) if i != line]
    elif operator == ">":
        value = [int(i) for i in range(0, 10) if i > line]
    elif operator == "<":
        value = [int(i) for i in range(0, 10) if i < line]
    elif operator == "<=":
        value = [int(i) for i in range(0, 10) if i <= line]
    elif operator == ">=":
        value = [int(i) for i in range(0, 10) if i >= line]
    return value


def main():
    """ Main function """
    line_1 = input()
    line_2 = input()
    line_3 = input()

    operator_line_1 = line_1.split()[0]
    operator_line_2 = line_2.split()[0]
    operator_line_3 = line_3.split()[0]

    value_line1 = calculate_of_line(operator_line_1, int(line_1.split()[1]))
    value_line2 = calculate_of_line(operator_line_2, int(line_2.split()[1]))
    value_line3 = calculate_of_line(operator_line_3, int(line_3.split()[1]))

    for axis_line3 in value_line3:
        for axis_line2 in value_line2:
            for axis_line1 in value_line1:
                print(str(axis_line3) + str(axis_line2) + str(axis_line1))


main()
