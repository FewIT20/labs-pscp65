"""IG: few.pz"""
def fibonacci(idx):
    """ Fibonacci function """
    if idx <= 0:
        return abs(idx)
    return fibonacci(idx-1) + fibonacci(idx-2)

def main():
    """ Main function """
    value = int(input())
    print(fibonacci(value))
main()
