"""IG: few.pz"""
def calculate_length(num):
    """Calculate the length of the value"""
    value = []
    while num != 1:
        value.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    value.append(1)
    return len(value)

def main():
    """ Main function """
    arr = []
    while True:
        value = int(input())
        if value == 0:
            break
        arr.append(value)
    for i in arr:
        print(calculate_length(i))
main()
