"""IG: few.pz"""
def main():
    """ Main function """
    mickey_home = int(input())
    list_mickey = []
    list_home = []
    list_max = []
    for _ in range(mickey_home):
        mickey = int(input())
        list_mickey.append(mickey)
    for _ in range(mickey_home):
        home = int(input())
        list_home.append(home)
    list_mickey.sort()
    list_home.sort()
    for i in range(mickey_home):
        value_max = (abs(int(list_mickey[i])-int(list_home[i])))
        list_max.append(value_max)
    print(max(list_max))
main()
