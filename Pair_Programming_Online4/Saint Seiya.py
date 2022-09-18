"""IG: few.pz"""
def main():
    """Main function"""
    second = int(input())
    push = int(input())

    counter = 0
    for i in range(2, second+1, 2):
        if counter < push:
            if i % 6 == 0:
                counter += 1
            elif i % 2 == 0:
                counter += 165
        else:
            counter += (second+1-i)*12
            break
    print(counter)
main()
