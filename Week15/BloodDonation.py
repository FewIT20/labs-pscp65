"""IG: few.pz"""
def can_donation(age, weight, count_of_donations, checked):
    """ Can blood donation function """
    value = False
    if (age == 17 or 60 <= age <= 70) and checked == 'False':
        value = False
    elif (count_of_donations == 0 and age > 55) or age < 17 or age > 70 or weight < 45:
        value = False
    elif (age == 17 or 60 <= age <= 70) and checked == 'True' and weight >= 45:
        value = True
    elif 17 < age < 60 and weight >= 45:
        value = True
    return value

def main():
    """ Main function """
    age = int(input())
    weight = int(input())
    count_of_donations = int(input())
    checked = False
    if age == 17 or 60 <= age <= 70:
        checked = input()
    result = can_donation(age, weight, count_of_donations, checked)
    if result:
        print("Yes")
    else:
        print("No")
main()
