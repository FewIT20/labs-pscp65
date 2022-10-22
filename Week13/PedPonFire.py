"""IG: few.pz"""
import math

def main():
    """ Main function """
    total = int(input())
    duck = []
    for _ in range(total):
        duck.append(int(input()))
    abstract = int(input())
    duck.sort()
    set_duck = sorted(set(duck))
    check = duck.count(abstract / 2)
    answer = 0 if check <= 1 else math.factorial(check) // (math.factorial(check - 2) \
        * math.factorial(2))
    for i in set_duck:
        if i >= abstract / 2:
            break
        answer += duck.count(abstract - i) * duck.count(i)
    print(answer)
main()
