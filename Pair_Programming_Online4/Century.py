"""IG: few.pz"""
import math

def calculate_year(year):
    """Calculate year"""
    if year < 1:
        return 'ERROR'
    elif year >= 1 and year <= 100:
        return 1
    else:
        return int(math.ceil(year / 100))

def main():
    """Main function"""
    value = int(input())
    for _ in range(value):
        idx = input()
        idx1 = idx[idx.count(". ") + 4 : len(idx)]
        year = int(idx1)
        if idx.count("B.E.") >= 1:
            year -= 543
            print(calculate_year(year))
        elif idx.count("A.D.") >= 1:
            print(calculate_year(year))
main()
