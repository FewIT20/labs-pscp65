"""IG: few.pz"""
def isprime(number):
    """ Find that number is prime or not """
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def circular(number):
    """ Find that is circular or not """
    if not isprime(number):
        return 0
    number_str = str(number)
    digits = len(number_str) - 1
    for _ in range(digits):
        number_str = number_str[-1] + number_str[:-1]
        if not isprime(int(number_str)):
            return 0
    return number

def main():
    """ Main function """
    number = int(input())
    result = [circular(x) for x in range(1, number + 1)]
    print(sum(result))
main()
