"""IG: few.pz"""
def main():
    """Main function"""
    weight = float(input())
    height = float(input())

    bmi = weight/(height/100)**2

    value = ""
    if bmi < 18.5:
        value = "Underweight"
    elif bmi < 25:
        value = "Normal"
    elif bmi < 30:
        value = "Overweight"
    elif bmi >= 30:
        value = "Obese"
    print(value)

main()
