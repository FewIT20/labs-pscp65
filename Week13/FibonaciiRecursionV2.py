"""IG: few.pz"""
def _fibonacci(fib_max_number):
    """Calculate  function"""
    x, y = 0, 1
    while x < fib_max_number:
        yield x
        x, y = y, x + y

def main():
    """ Main function """
    fib_max_number = int(input())
    fib_list = [n for n in _fibonacci(999999999999999999999999999999999999)]
    print(fib_list[fib_max_number])
main()