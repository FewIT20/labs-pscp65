"""IG: few.pz"""
def main():
    """Main function"""
    count = int(input())
    for _ in range(count):
        next_value = int(input())
        value = []
        for _ in range(next_value):
            text = input().split()
            changed_integer_to_list = []
            changed_integer_to_list.append(int(text[0]))
            changed_integer_to_list.append(int(text[1]))
            value.append(changed_integer_to_list)
        value.sort(reverse=True, key=lambda value: value[1])
        value.sort(key=lambda value: value[0]+value[1])
        for i in value:
            for j in i:
                print(j, end=" ")
            print()
main()
