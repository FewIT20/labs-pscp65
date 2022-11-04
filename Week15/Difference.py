"""IG: few.pz"""
import json

def main():
    """ Main function """
    lst_1 = json.loads(input())
    lst_2 = json.loads(input())
    set_1 = set(lst_1)
    set_2 = set(lst_2)
    check = set_1.union(set_2)
    count = 0
    for i in sorted(check):
        if abs(lst_1.count(i) - lst_2.count(i)) != 0:
            print(i, abs(lst_1.count(i) - lst_2.count(i)))
            count += 1
    if count == 0:
        print("ONAJI DAYO!")
main()
