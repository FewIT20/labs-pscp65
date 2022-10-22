"""IG: few.pz"""
def checked(num):
    """ Check if number is square free """
    if num % 2 == 0:
        num /= 2
    if num % 2 == 0:
        return False
    for i in range(3, int((num**0.5)+1)):
        if num % i == 0:
            num /= i
        if num % i == 0:
            return False
    return True

def main():
    """ Main function """
    count = 0
    for i in range(1, int(input())+1):
        if checked(i):
            count += 1
    print(count)
main()
