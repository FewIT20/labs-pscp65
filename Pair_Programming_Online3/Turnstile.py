"""IG: few.pz"""
def main():
    """Main function"""
    kick_in_the_door_waving_co_co = 0
    people = 0
    while True:
        action = input().lower()
        if action == "end":
            break
        if action == "c":
            kick_in_the_door_waving_co_co = 1
        if action == "p":
            if kick_in_the_door_waving_co_co == 1:
                people = people + 1
            kick_in_the_door_waving_co_co = 0
    print(people)
main()
