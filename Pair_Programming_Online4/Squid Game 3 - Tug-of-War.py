"""IG: few.pz"""
def main():
    """Main function"""
    team_a = 0
    team_b = 0
    for _ in range(10):
        team_a += int(input())
    for _ in range(10):
        team_b += int(input())
    if team_a == team_b:
        print('AB')
    elif team_a > team_b:
        print('B')
    elif team_a < team_b:
        print('A')
main()
