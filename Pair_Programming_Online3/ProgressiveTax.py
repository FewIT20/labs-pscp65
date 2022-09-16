"""IG: few.pz"""
def main():
    """Main function"""
    salary = int(input())
    tax = 0
    if salary > 4000000:
        calc_salary = salary - 4000000
        salary -= calc_salary
        tax += calc_salary * 0.35
    if salary > 2000000:
        calc_salary = salary - 2000000
        salary -= calc_salary
        tax += calc_salary * 0.30
    if salary > 1000000:
        calc_salary = salary - 1000000
        salary -= calc_salary
        tax += calc_salary * 0.25
    if salary > 750000:
        calc_salary = salary - 750000
        salary -= calc_salary
        tax += calc_salary * 0.20
    if salary > 500000:
        calc_salary = salary - 500000
        salary -= calc_salary
        tax += calc_salary * 0.15
    if salary > 300000:
        calc_salary = salary - 300000
        salary -= calc_salary
        tax += calc_salary * 0.10
    if salary > 150000:
        calc_salary = salary - 150000
        salary -= calc_salary
        tax += calc_salary * 0.05
    if salary > 0:
        pass
    print(int(tax))
main()
