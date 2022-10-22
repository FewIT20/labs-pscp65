"""IG: few.pz"""
def fibonacci(number):
    """ Return fibonacci values for given number """
    data = {0:0, 1:1}
    if number in data:
        return data[number]
    if number > 500:
        fibonacci(number - 500)
    res = fibonacci(number-2) + fibonacci(number-1)
    data[number] = res
    return res

def main():
    """ Main function """
    number = int(input())
    result = fibonacci(number)
    print(result)
main()
