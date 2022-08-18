"""IG: few.pz"""

def main():
    """Main function"""
    int(input())
    x_var = input().split(" ")
    arr = [float(i) for i in x_var]
    arr = sorted(arr)
    arr2 = []
    for _ in range(0, len(arr) // 2):
        # find closest
        var = arr.pop(0)
        var3 = False
        diff = 0
        closestnum = 0
        for i in range(0, len(arr)):
            checking = arr[i]
            if var3 == False:
                var3 = True
                diff = abs(checking - var)
                closestnum = checking
                continue
            diff2 = abs(checking - var)
            if diff2 < diff:
                closestnum = checking
                diff = diff2
        #
        arr.remove(closestnum)
        arr2.append(diff)
    #
    arr2 = sorted(arr2)
    arr2.pop(-1)
    value = sum(arr2)
    print(str(int(value)))

main()
