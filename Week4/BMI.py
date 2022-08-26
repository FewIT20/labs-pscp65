"""IG: few.pz"""
def calc_body_mass_index(x_val):
    """Calculate body mass index"""
    weight = x_val[1]
    hight = x_val[2]
    bmi = weight / (hight/100)**2
    print("%s's  BMI = %.2f" % (x_val[0], (bmi)))

def main():
    """Main function"""
    players = []
    for _ in range(1, 6):
        name = input()
        weight = float(input())
        hight = float(input())
        players.append([name, weight, hight])
    for x_val in players:
        calc_body_mass_index(x_val)
main()
