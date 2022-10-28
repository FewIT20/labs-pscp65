"""IG: few.pz"""
def main(num):
    """isPrime_large"""
    if num == 1:
        return "False"
    for i in range(2, int(num**0.5)+1, 3):
        if num % i == 0:
            return "False"
    return "True"
print(main(int(input())))
