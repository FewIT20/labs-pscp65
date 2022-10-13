"""IG: few.pz"""
def main():
    """Main function"""
    list_group1 = set()
    list_group2 = set()
    num_m = int(input())
    num_n = int(input())
    for _ in range(num_m):
        data_m = input()
        list_group1.add(data_m)
    for _ in range(num_n):
        data_n = input()
        list_group2.add(data_n)
    ans = list_group1.intersection(list_group2)
    ans_real = (sorted((ans), reverse=True))
    if ans == set():  #set()
        print("Nope")
    else:
        for i in ans_real:
            print(i)
main()
