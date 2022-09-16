"""IG: few.pz"""
def main():
    """Main function"""
    x_val = int(input())
    y_val = int(input())
    type_player = input()
    if type_player == "A":
        elo = 1/(1+(10**((y_val-x_val)/400)))
    elif type_player == "B":
        elo = 1/(1+(10**((x_val-y_val)/400)))
    print("%.2f" %elo)
main()
