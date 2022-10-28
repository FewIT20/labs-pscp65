"""IG: few.pz"""
def main():
    """ Main function """
    number_total = int(input())
    number_list = []
    for _ in range(number_total):
        number = int(input())
        number_list.append(number)
    max_number = max(number_list)
    gcd_value = 0
    for i in range(1, max_number+1):
        dividable = 0
        for number in number_list:
            if number % i == 0:
                dividable += 1
        if dividable == number_total:
            gcd_value = i
    print(gcd_value)
main()
