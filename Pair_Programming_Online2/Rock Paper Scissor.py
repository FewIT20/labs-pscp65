"""IG: few.pz"""
def gameplay(value, a_point, b_point):
    """"Gameplay function"""
    if value[:1] == 'R':
        if value[1:] == 'P':
            b_point += 1
        else:
            a_point += 1
    if value[:1] == 'S':
        if value[1:] == 'P':
            a_point += 1
        else:
            b_point += 1
    if value[:1] == 'P':
        if value[1:] == 'R':
            a_point += 1
        else:
            b_point += 1
    return a_point, b_point

def main():
    """Main function"""
    value = str(input())
    x_val = ''
    y_val = []
    player_a_point = 0
    player_b_point = 0

    for z_val in value:
        if len(x_val) == 1:
            if x_val == z_val:
                x_val = ''
                continue
            x_val += z_val
            y_val.append(x_val)
            x_val = ''
        else:
            x_val += z_val
    for count in range(len(y_val)):
        player_a_point, player_b_point = gameplay(y_val[count], player_a_point, player_b_point)
    if player_a_point == player_b_point:
        print("DRAW %d" %(player_a_point))
    elif player_a_point > player_b_point:
        print("A win %d-%d" %(player_a_point, player_b_point))
    elif player_b_point > player_a_point:
        print("B win %d-%d" %(player_b_point, player_a_point))
main()
