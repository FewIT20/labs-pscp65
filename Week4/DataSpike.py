"""IG: few.pz"""
def maimum(var_a, var_b):
    """Find the maximum value"""
    if var_a >= var_b:
        return var_a
    else:
        return var_b

def main():
    """Main function"""
    var_1 = int(input())
    var_2 = int(input())

    total = maimum(var_1, var_2)
    var_3 = int(input())
    total = maimum(total, var_3)
    var_4 = int(input())
    total = maimum(total, var_4)
    var_5 = int(input())
    total = maimum(total, var_5)
    var_6 = int(input())
    total = maimum(total, var_6)
    var_7 = int(input())
    total = maimum(total, var_7)
    var_8 = int(input())
    total = maimum(total, var_8)
    print(total)
main()
