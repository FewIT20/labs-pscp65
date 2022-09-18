"""IG: few.pz"""
def main():
    """Main function"""
    border_top = input()
    pringle = input()
    border_bottom = input()
    value = int(input())

    eat_count = 0
    left_count = 0
    eat = pringle[:value:]
    left = pringle[value::]

    for i in eat:
        if i == ")":
            eat_count = eat_count + 1
    for i in left:
        if i == ")":
            left_count = left_count + 1

    print(eat_count)
    if left_count == 0:
        print("None.")
    else:
        print("There are still some left.")

    print(border_top)
    print("%s%s" %((" "*value), pringle[value:]))
    print(border_bottom)
main()
