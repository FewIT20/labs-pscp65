"""IG: few.pz"""
 
 
def calc_body_mass_index(weight, hight):
    """Calculate body mass index"""
    bmi = weight/(hight/100)**2
    return bmi
 
 
def main():
    """Main function"""
    player_1 = input()
    player_1_height = float(input())
    player_1_weight = float(input())
    player_2 = input()
    player_2_height = float(input())
    player_2_weight = float(input())
    player_3 = input()
    player_3_height = float(input())
    player_3_weight = float(input())
    player_4 = input()
    player_4_height = float(input())
    player_4_weight = float(input())
    player_5 = input()
    player_5_height = float(input())
    player_5_weight = float(input())
 
    print("%s's  BMI = %.2f" %
          (player_1, (calc_body_mass_index(player_1_height, player_1_weight))))
    print("%s's  BMI = %.2f" %
          (player_2, (calc_body_mass_index(player_2_height, player_2_weight))))
    print("%s's  BMI = %.2f" %
          (player_3, (calc_body_mass_index(player_3_height, player_3_weight))))
    print("%s's  BMI = %.2f" %
          (player_4, (calc_body_mass_index(player_4_height, player_4_weight))))
    print("%s's  BMI = %.2f" %
          (player_5, (calc_body_mass_index(player_5_height, player_5_weight))))
 
 
main()
