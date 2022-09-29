"""IG: few.pz"""
from codecs import charmap_encode


def main():
    """Main function"""
    a, b, c = [int(value) for value in input().split()]
    text = input()
    arr = []
    arr.append(a) 
    arr.append(b)
    arr.append(c)
    arr.sort()
    for character in text:
        if character == "A":
            print(arr[0], end=" ")
        elif character == "B":
            print(arr[1], end=" ")
        elif character == "C":
            print(arr[2], end=" ")

main()
