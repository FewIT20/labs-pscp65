"""IG: few.pz"""
def main():
    """Main function"""
    meteorite = float(input())
    more_meteorite = int(input())
    safe_of_weight = float(input())
    increment, total_missile = 0, 0
    if meteorite < safe_of_weight:
        total_missile = 0
    else:
        while not meteorite < safe_of_weight:
            meteorite = meteorite / more_meteorite
            total_missile += more_meteorite**increment
            increment += 1
    print(total_missile)
main()
