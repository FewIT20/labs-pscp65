"""IG: few.pz"""
def main():
    """Main function"""
    num = int(input())
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main()
