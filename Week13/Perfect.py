"""IG: few.pz"""
def isprime(number):
    """ Find that number is prime or not """
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def perfect(number):
    """ Calculate that is perfect number or not """
    perfects = []
    for count in range(2, number):
        if isprime(count):
            perfect_number = (2 ** (count - 1)) * ((2 ** count) - 1)
            if perfect_number > number:
                break
            elif perfect_number <= number and perfect_number not in perfects:
                perfects.append(perfect_number)
    return sum(perfects)

def main():
    """ Main function """
    number = int(input())
    print(perfect(number))
main()
