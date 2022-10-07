"""IG: few.pz"""
def main():
    """Main function"""
    sequence = tuple(input().split(" "))
    find_index = input()
    for _ in range(sequence.count(find_index)):
        for _ in range(sequence.count(find_index)):
            print(int(sequence.index(find_index)), end=" ")
        print()
main()
