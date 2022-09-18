"""IG: few.pz"""
def main():
    """Main function"""
    idx1 = 0
    idx2 = 0
    result = ''
    while True:
        value = int(input())
        if value == -1:
            if result == '':
                result = str(idx1) if idx1 == (idx1 + idx2) \
else str(idx1) + '-' + str(idx1 + idx2)
            else:
                result = result + ', ' + str(idx1) if idx1 == (idx1 + idx2) else result + \
', ' + str(idx1) + '-' + str(idx1 + idx2)
            break
        if idx1 != value:
            if idx1 == 0:
                idx1 = value
            elif (idx1 + idx2 + 1) == value:
                idx2 += 1
            else:
                if result == '':
                    result = str(idx1) if idx1 == (idx1 + idx2) else str(idx1) + \
'-' + str(idx1 + idx2)
                else:
                    result = result + ', ' + str(idx1) if idx1 == (idx1 + idx2) else result + \
', ' + str(idx1) + '-' + str(idx1 + idx2)
                idx1 = value
                idx2 = 0
    print('' if result == '0' else result)
main()
