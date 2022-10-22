"""IG: few.pz"""
def main():
    """ Main function """
    turn = 0
    warm = 0
    count = 0
    last = 0
    while True:
        time = input()
        if time == "End":
            break
        time = float(time)
        if time == 0:
            turn = 1
            continue
        if turn == 1:
            turn = 0
            last = time
            continue
        if turn == 0 and time - last > 6:
            warm = 0
            turn = 1
        if turn == 0 and time - last <= 6 and warm == 0:
            warm = 1
            turn = 1
            count += 1
        if turn == 0 and time - last <= 6 and warm == 1:
            warm = 0
            turn = 1
    print(count)
main()
