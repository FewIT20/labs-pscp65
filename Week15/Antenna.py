"""IG: few.pz"""
import json

def main():
    """ Main function """
    radius = int(input())
    people = sorted(json.loads(input()))
    limit = 0
    count = 1
    if not people:
        return print("0")
    limit = people.pop(0)+(radius*2)
    while people:
        new_people = people.pop(0)
        if new_people > limit:
            count += 1
            limit = new_people+radius*2
    print(count)
main()
