"""IG: few.pz"""
def closest(position):
    """ Keep position """
    num_min = position[1] - position[0]
    position_1 = 0
    position_2 = 1
    for i in range(len(position)-1):
        if position[i+1] - position[i] < num_min:
            num_min = position[i+1] - position[i]
            position_1 = i
            position_2 = i+1
    return num_min, position_1, position_2

def main():
    """ Main function """
    number = int(input())
    weight = input().split()
    position = []
    num_min, position_1, position_2 = 0, 0, 0
    summation = 0
    for i in range(len(weight)):
        position.append(int(weight[i]))
    position.sort()
    for _ in range(number-1):
        num_min, position_1, position_2 = closest(position)
        summation += num_min
        position.remove(position[position_2])
        position.remove(position[position_1])
    print(summation)

main()
