"""IG : few.pz"""
def main():
    """ Main function """
    bowls = input().replace(" ", "")
    points = 0
    for i in range(0, len(bowls)):
        bowl = bowls[i]
        count_next_bowls = 0
        if bowl.isdigit():
            points += get_points(bowl)
        elif bowl == '/':
            points += 10 - get_points(bowls[i-1])
            count_next_bowls = 1
        elif bowl == 'X':
            points += get_points(bowl)
            count_next_bowls = 2
        if i < (len(bowls) - 3) and count_next_bowls > 0:
            j = i+1
            while count_next_bowls > 0:          
                next_bowl = bowls[j]
                if next_bowl == '/':
                    points += 10 - get_points(bowls[j-1])
                else:
                    points += get_points(next_bowl)
                j += 1
                count_next_bowls -= 1
    print("%i" % points)
               
def get_points(symbol):
    if symbol.isdigit():
        return int(symbol)
    elif symbol == 'X':
        return 10
    return 0

main()
