"""IG: few.pz"""
def main():
    """ Main function """
    num = int(input())
    coder = ""
    decoder = {"1":"papan", "2":"dogugu", "3":"gushigi", "4":"zugogo", "5":"zugagi", \
        "6":"gibugu", "7":"gezun", "8":"gegido", "9":"bagin", "+":"do ", "*":"gu ", "0":"zezeso"}
    group, new_group = [], []
    count = 0
    while num > 9:
        if num % 9 != 0:
            group.insert(0, str(num % 9))
            num -= num % 9
        num = num // 9
        count += 1
    group.insert(0, str(num))
    for i in range(len(group)):
        new_group.append("9*"*count+group[i])
        count -= 1
    encoder = "+".join(new_group).replace("*1", "")
    for i in encoder:
        coder += decoder[i]
    print(coder)
main()
