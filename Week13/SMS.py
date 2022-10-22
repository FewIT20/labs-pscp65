"""IG: few.pz"""
def main():
    """ Main function """
    lis = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], \
["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
    value = []
    for _ in range(int(input())):
        num1 = int(input())
        num2 = int(input())
        if num1 == 1:
            for _ in range(num2):
                if len(value) > 0:
                    value.pop()
        if num1 == 2 or num1 == 3 or num1 == 4 or num1 == 5 or num1 == 6 or num1 == 8 and num2 != 0:
            if num2 % 3 == 0:
                value.append(lis[num1-2][2])
            else:
                value.append(lis[num1-2][(num2 % 3)-1])
        if num1 == 7 or num1 == 9:
            if num2 % 4 == 0:
                value.append(lis[num1-2][3])
            else:
                value.append(lis[num1-2][(num2 % 4)-1])
    if len(value) > 0:
        return print(*value, sep="")
    print("null")
main()
